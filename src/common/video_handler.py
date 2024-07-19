from pathlib import Path

import cv2

from src.common.ffmpeg_handler import FFmpegHandler
from src.common.processors.audio_processors.audio_processor_manager import AudioProcessorManager
from src.common.processors.opencv_processors.opencv_processor_manager import OpenCVProcessorManager
from src.common.processors.processor_global_var import ProcessorGlobalVar
from src.core.enums import Orientation
from src.signal_bus import SignalBus
from src.utils import TempDir, get_output_file_path


class VideoHandler:
    def __init__(self):
        self._signal_bus: SignalBus = SignalBus()
        self._temp_dir: TempDir = TempDir()
        self._ffmpeg_handler: FFmpegHandler = FFmpegHandler()
        self._audio_processor_manager: AudioProcessorManager = AudioProcessorManager()
        self._video_processor_manager: OpenCVProcessorManager = OpenCVProcessorManager()

    def process_video(self, input_video_path: Path,) -> Path:
        video_after_processed = self._video_process(input_video_path)

        audio_extractor = self._ffmpeg_handler.extract_audio_from_video(input_video_path)
        audio_after_processed = self._audio_process(audio_extractor, self._audio_processor_manager)
        # 合并视频和音频
        return self._ffmpeg_handler.replace_video_audio(video_after_processed, audio_after_processed)

    def merge_videos(self, video_list: list[Path]):
        ...

    def compress_video(self, input_video_path: Path, output_video_path: Path):
        ...

    def _video_process(self, input_video_path: Path,) -> Path:
        """
        读取输入视频，逐帧处理，然后写入输出视频,以及音频处理

        Args:
            input_video_path: 输入视频的路径
        """
        cap = cv2.VideoCapture(str(input_video_path))
        if not cap.isOpened():
            raise ValueError("无法打开输入视频")

        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # 因为处理后的视频的宽高可能会发生变化，所以需要重新获取宽高
        width, height = self._get_after_process_width_and_height(input_video_path)

        # MP4V比较通用，但是不支持透明度
        fourcc = cv2.VideoWriter.fourcc(*'mp4v')
        output_file_path = get_output_file_path(input_video_path, "video_processed")
        out = cv2.VideoWriter(str(output_file_path), fourcc, fps, (width, height))

        for _ in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break

            # 对帧进行处理
            processed_frame = self._video_processor_manager.process(frame)

            # 写入处理后的帧
            out.write(processed_frame)

        # 释放资源
        cap.release()
        out.release()
        return output_file_path

    def _audio_process(self, input_video_path: Path,
                       processor_manager: AudioProcessorManager) -> Path:
        """
        读取输入视频，逐帧处理，然后写入输出视频,以及音频处理

        Args:
            input_video_path: 输入视频的路径
            processor_manager: 用于处理音频的处理器
        """
        output_file_path = get_output_file_path(input_video_path, "audio_processed")
        processor_manager.process(input_video_path)
        return output_file_path

    def _get_after_process_width_and_height(self,input_video_path: Path,) -> tuple[int, int]:
        cap = cv2.VideoCapture(str(input_video_path))
        if not cap.isOpened():
            raise ValueError("无法打开输入视频")

        ret, frame = cap.read()
        if not ret:
            raise ValueError("无法读取视频的第一帧")
        processed_frame = self._video_processor_manager.process(frame)

        height, width = processed_frame.shape[:2]
        cap.release()
        return width, height


if __name__ == '__main__':
    v = VideoHandler()
    global_var = ProcessorGlobalVar()
    global_var.update("crop_x", 0)
    global_var.update("crop_y", 515)
    global_var.update("crop_width", 716)
    global_var.update("crop_height", 482)
    global_var.update("rotation_angle", 90)
    global_var.update("orientation", Orientation.HORIZONTAL)
    global_var.update("target_width", 500)
    global_var.update("target_height", 300)

    print(v.process_video(Path(r"E:\load\python\Project\VideoFusion\TempAndTest\dy\v\1\视频  (3).mp4")))
