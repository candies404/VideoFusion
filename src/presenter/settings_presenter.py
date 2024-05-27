import loguru
from PySide6.QtWidgets import QFileDialog

from src.config import cfg
from src.model.settings_model import SettingsModel
from src.view.settings_view import SettingView


class SettingsPresenter:
    def __init__(self):
        self._view: SettingView = SettingView()
        self._model: SettingsModel = SettingsModel()
        self._connect_signal()

    def get_view(self) -> SettingView:
        return self._view

    def get_model(self) -> SettingsModel:
        return self._model

    def _select_ffmpeg_file(self):
        # 选择ffmepg.exe的路径
        file_path, _ = QFileDialog.getOpenFileName(self._view, "选择FFmpeg.exe", "", "ffmpeg.exe (*.exe)")
        if file_path:
            cfg.set(cfg.ffmpeg_file, file_path)
            loguru.logger.info(f"选择了FFmpeg路径: {file_path}")
            return
        self.get_view().show_error_infobar("错误", "请选择一个有效的FFmpeg路径", duration=3000, is_closable=True)

    def _select_temp_dir(self):
        # 选择临时目录的路径
        dir_path = QFileDialog.getExistingDirectory(self._view, "选择临时目录", "")
        if dir_path:
            cfg.set(cfg.temp_dir, dir_path)
            loguru.logger.info(f"选择了临时目录: {dir_path}")
            return
        self.get_view().show_error_infobar("错误", "请选择一个有效的临时目录", duration=3000, is_closable=True)

    def _select_output_file_path(self):
        # 选择输出文件保存的位置
        output_file_path = QFileDialog.getSaveFileName(self._view, "选择输出文件路径", "输出文件.mp4",
                                                       "视频文件 (*.mp4)")
        if output_file_path[0]:
            cfg.set(cfg.output_file_path, output_file_path[0])
            loguru.logger.info(f"选择了输出文件路径: {output_file_path[0]}")
            return
        self.get_view().show_error_infobar("错误", "请选择一个有效的输出文件路径", duration=3000, is_closable=True)

    def _connect_signal(self):
        self._view.ffmpeg_file_card.clicked.connect(self._select_ffmpeg_file)
        self._view.temp_dir_card.clicked.connect(self._select_temp_dir)
        self._view.output_file_path_card.clicked.connect(self._select_output_file_path)