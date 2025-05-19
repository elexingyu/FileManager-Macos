"""UI工具模块，提供UI相关的通用功能"""
import platform
from tkinter import messagebox as mBox
from core.logger import logger


# 安全的消息框显示函数，处理macOS上的TclError
def safe_showinfo(title, message, text_widget=None):
    """
    安全地显示消息框，如果失败则记录到日志
    
    Args:
        title: 消息框标题
        message: 消息框内容
        text_widget: 文本控件，若提供则在其中也显示消息
    """
    if text_widget:
        text_widget.insert('end', f"\n{message}\n")
        text_widget.see('end')
    
    try:
        mBox.showinfo(title, message)
    except Exception as e:
        # 捕获TclError或其他异常，仅记录错误但不影响程序流程
        logger.debug(f"显示消息框时出错: {str(e)}") 