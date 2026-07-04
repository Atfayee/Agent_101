from typing import Any

class ToolInputError(ValueError):
    """
    用户 或 LLM 传入了错误参数。
    这类错误通常允许 LLM 自我修正。
    """
    pass

class ToolTemporaryError(RuntimeError):
    """
    临时性系统错误。
    例如 timeout、rate limit、第三方服务短暂不可用。
    Lesson 2 会用 retry/backoff 处理。
    """
    pass

class ToolFataError(RuntimeError):
    """
    不可恢复错误。
    例如 API key 缺失、权限错误、系统配置错误。
    """
    pass

def format_tool_error(error: Exception) -> str:
    """
    把 Python exception 转成 LLM 可以理解的 tool error message。

    注意：
    这里不要暴露敏感信息，例如 API key、数据库连接串、内部路径。
    """

    if isinstance(error, ToolInputError):
        return (
            "TOOL_INPUT_ERROR: The tool arguments are invalid. "
            f"Reason: {str(error)}"
            "Please correct the arguments and call the tool again."
        )
    if isinstance(error, ToolTemporaryError):
        return (
            "TOOL_TEMPORARY_ERROR: The tool failed because of a temporary system issue."
            f"Reason: {str(error)}"
            "You may retry later or use another avaliable tool."
        )
    if isinstance(error, ToolFataError):
        return (
            "TOOL_FATA_ERROR: The tool cannot continue because of a system configuration issue."
            "Do not retry this exact tool call. Explain the issue to the user or use a fallback path."
        )
    
    return (
        "TOOL_UNKNOWN_ERRIR: The tool railed unexpectedly"
        "Do not invent results. Explain that the tool failed or try a safer alternative."
    )


