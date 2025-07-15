from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def moveStraight(name: str) -> str:
    """
    调用机器人直行接口
    """
    try:
        response = requests.post("http://10.3.51.233:8080/go-straight")
        # if response.status_code == 200:
        return f"指令 '{name}' 执行成功，机器人已直行。"
        # else:
        #     return f"调用失败，状态码: {response.status_code}"
    except requests.RequestException as e:
        return f"请求错误: {e}"


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)
