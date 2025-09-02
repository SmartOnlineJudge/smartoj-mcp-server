# 智能算法刷题平台——MCP 服务器代码仓库

## 🖼️仓库介绍

当前仓库是专门为智能算法平台而开发的，目的是为了能让大模型调用该项目的部分后端接口，以实现一些智能化的功能，例如：自动完善题库、自动规划用户的刷题路线、大模型自动判题等等功能。

## ❓相关问题

### 为什么不直接使用 FastMCP 直接将后端接口转换成 MCP 工具？

项目的后端是基于 FastAPI 框架进行构建，它的每一个接口天生符合 OpenAPI 接口规范，而 FastMCP 也支持直接从 OpenAPI 文档中直接定义 MCP 工具，因此该项目后端的每一个接口都可以直接使用 FastMCP 库转换成相应的 MCP 工具。

```python
from fastapi import FastAPI
from fastmcp import FastMCP

app = FastAPI()
mcp_server = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run()
```

官方文档：[FastAPI 🤝 FastMCP - FastMCP](https://gofastmcp.com/integrations/fastapi#generating-an-mcp-server)。

这个库极大程度上简化了开发的难度并减少了相应的开发成本，可以说几乎使用零成本就可以将后端的接口直接转换成 MCP 工具。

🤔但是为什么不推荐使用这样的方式转换呢？

经过仔细阅读 FastMCP 的官方文档，可以发现里面有一段这样的警告或建议：

> Generating MCP servers from OpenAPI is a great way to get started with FastMCP, but in practice LLMs achieve **significantly better performance** with well-designed and curated MCP servers than with auto-converted OpenAPI servers. This is especially true for complex APIs with many endpoints and parameters.We recommend using the FastAPI integration for bootstrapping and prototyping, not for mirroring your API to LLM clients. See the post [Stop Converting Your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp) for more details.

这段话主要想表达的意思是：直接使用 FastMCP 将后端接口转换成相应的 MCP 工具是一个非常便捷且高效的方式，但是人为编写一个高效且易于大模型理解的 MCP 服务器比直接使用这种方式得到的 MCP 服务器会更加高效且更有利于大模型调用。并且在最后给出了一篇文章来进一步加强这个建议的程度。

那篇文章的意思也很简单，它大概从以下几点来建议我们不要直接将 Restful 风格的 API 转换成大模型使用的工具：

1. **信息过载**：
   - REST API 通常提供大量细粒度、原子化的端点，适合人类开发者组合使用。
   - 对 LLM 来说，每个工具都会增加上下文负担（token 和延迟），导致决策困难。
2. **交互效率低**：
   - LLM 每次调用工具都需要完整的推理周期，链式调用多个小工具成本高昂。
   - 原子性对人友好，对 agent 是反模式。
3. **上下文污染**：
   - 工具过多会“淹没”模型，使其关注无关细节，偏离任务目标。
   - 导致模型变慢、变笨、更贵。

通过阅读这些信息，我仔细思考了一下现有的后端接口，确实有很多接口不应该给大模型来直接调用，因为有些接口的调用需要组合调用以及人为干预，一旦大模型出现调用失误，一方面对用户不友好，另一方面也有可能会暴露部分系统的敏感信息。

总的来说，现有的后端接口是按照人类能够理解的方式来编写的，但是大模型可能会无法理解这些接口的含义或者调用方式。而目前绝大多数知名 MCP 服务器也都是重新编写，而非直接使用相关的工具将相应的后端接口映射成 MCP 工具。例如：GitHub、百度地图等等知名 MCP 服务器。

所以按照现有的后端接口重新编写一个 MCP 服务器是一个较为正确且明智的选择。

## 🔧工具列表

