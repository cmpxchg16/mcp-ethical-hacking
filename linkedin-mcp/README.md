
# MCP linkedin

An MCP server that lets you interact with Linkedin discussions without the need for an API key from an external service.

## Usage

Start the server using stdio (default):

```bash
# Using stdio transport (default)
uv run linkedin-mcp
```

The server exposes a tool named "linkedin_analyze" that accepts two required arguments:

- `url`: The URL of the linkedin profile to fetch e.g: https://www.linkedin.com/in/cmpxchg16
- `cookies`: Linkedin Cookies extracted by Chrome Extension

## Example

You can use test with a local MCP client before Claude Desktop:

```bash
uv run client.py
```

## Integrate with Claude Desktop

In the repo you will find [claude_desktop_config.json](./claude_desktop_config.json) the file to put in Claude Desktop, just change the params accordingly:

```json
{
    "mcpServers": {
        "linkedin": {
            "command": "CHANGEME_TO_HOME/.local/bin/uv",
            "args": [
                "--directory",
                "CHANGEME_TO_REPO_DIR/linkedin-mcp/",
                "run",
                "linkedin-mcp"
            ]
        }
    }
}
```
You can read more here:

https://modelcontextprotocol.io/quickstart/user

