
# MCP Reddit

An MCP server that lets you interact with Reddit discussions without the need for an API key from an external service.

## Usage

Start the server using stdio (default):

```bash
# Using stdio transport (default)
uv run reddit-mcp
```

The server exposes a tool named "reddit_extract" that accepts one required argument:

- `url`: The URL of the reddit discussion to fetch e.g: https://www.reddit.com/r/ChatGPTCoding/comments/1hy3683/this_sub_in_a_nutshell/

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
        "reddit": {
            "command": "CHANGEME_TO_HOME/.local/bin/uv",
            "args": [
                "--directory",
                "CHANGEME_TO_REPO_DIR/reddit-mcp/",
                "run",
                "reddit-mcp"
            ]
        }
    }
}
```
You can read more here:

https://modelcontextprotocol.io/quickstart/user