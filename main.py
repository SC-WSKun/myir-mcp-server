from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def moveToA(name: str) -> str:
    """
    调用机器人去A点的接口
    """
    try:
        response = requests.post("http://myir:8080/go-to-a")
        # if response.status_code == 200:
        return f"指令 '{name}' 执行成功，机器人已直行。"
        # else:
        #     return f"调用失败，状态码: {response.status_code}"
    except requests.RequestException as e:
        return f"请求错误: {e}"

@mcp.tool
def moveToB(name: str) -> str:
    """
    调用机器人去B点的接口
    """
    try:
        response = requests.post("http://myir:8080/go-to-b")
        # if response.status_code == 200:
        return f"指令 '{name}' 执行成功，机器人已返回。"
        # else:
        #     return f"调用失败，状态码: {response.status_code}"
    except requests.RequestException as e:
        return f"请求错误: {e}"

@mcp.tool
def moveBack(name: str) -> str:
    """
    调用机器人返回的接口
    """
    try:
        response = requests.post("http://myir:8080/go-back")
        # if response.status_code == 200:
        return f"指令 '{name}' 执行成功，机器人已返回。"
        # else:
        #     return f"调用失败，状态码: {response.status_code}"
    except requests.RequestException as e:
        return f"请求错误: {e}"

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=9000)
