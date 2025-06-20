# ⚡ MCP CrewLink

A powerful integration project that links Model Context Protocol (MCP) servers with CrewAI agents to enable AI assistants with enhanced capabilities including image generation, web search, and file system operations.

## 🚀 Features

- **Image Generation**: Create high-quality images using OpenAI's DALL-E 3 model
- **Web Search**: Perform web searches using Brave Search API
- **File System Operations**: Read, write, and manage files in specified directories
- **AI Agent Integration**: Leverage CrewAI for intelligent task execution and coordination
- **MCP Protocol**: Utilize the Model Context Protocol for seamless tool integration

## 📁 Project Structure

```
project-root/
├── main.py                 # Main application entry point
├── servers/
│   └── image_server.py     # Custom MCP server for image generation
├── images/                 # Generated images output directory (auto-created)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
└── README.md              # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### 1. Clone the Repository

```bash
git clone https://github.com/naakaarafr/MCP-CrewLink.git
cd MCP-CrewLink
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Node.js Dependencies

The project uses MCP servers that require Node.js packages:

```bash
# Install MCP filesystem server
npm install -g @modelcontextprotocol/server-filesystem

# Install MCP Brave search server
npm install -g @modelcontextprotocol/server-brave-search
```

### 4. Environment Setup

Create a `.env` file in the project root with the following variables:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ORGANIZATION=your_openai_organization_id_here

# Brave Search Configuration
BRAVE_API_KEY=your_brave_api_key_here
```

## 🔑 API Keys Setup

### OpenAI API Key
1. Visit [OpenAI API Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key to your `.env` file

### Brave Search API Key
1. Visit [Brave Search API](https://api.search.brave.com/)
2. Sign up for an account
3. Generate an API key
4. Copy the key to your `.env` file

## 🚀 Usage

### Running the Main Application

```bash
python main.py
```

### Running the Image Server Standalone

```bash
python servers/image_server.py
```

## 🔧 Components

### 1. Image Server (`servers/image_server.py`)

A custom MCP server that provides image generation capabilities using OpenAI's DALL-E 3.

**Features:**
- High-quality image generation (1024x1024, HD quality)
- Base64 image handling
- Automatic file saving
- Error handling and logging

**Usage Example:**
```python
# The server exposes the image_creation_openai tool
# Parameters: query (str), image_name (str)
# Returns: Dict with success status, file_path, and message
```

### 2. Main Application (`main.py`)

Orchestrates the integration between MCP servers and CrewAI agents.

**Configuration:**
- **Filesystem Server**: Manages files in `/Users/tylerreed/Downloads`
- **Brave Search Server**: Provides web search capabilities
- **Image Server**: Custom image generation server

**Agent Configuration:**
- Role: Creator
- Goal: AI Creator using MCP Tools
- Capabilities: Research, image creation, file management

## 📋 Example Tasks

The application includes example tasks that demonstrate the integration:

1. **Research Task**: Research Model Context Protocol and create an in-depth diagram
2. **Summary Task**: Summarize results and save to a text file

## 🔄 Workflow

1. **Initialization**: Configure MCP server parameters
2. **Agent Setup**: Create CrewAI agent with MCP tools
3. **Task Definition**: Define research and creation tasks
4. **Execution**: Run the crew to execute tasks
5. **Output**: Generate images, perform searches, and save results

## 🛡️ Error Handling

The project includes comprehensive error handling:

- **Image Generation**: Catches API errors and file system issues
- **Server Communication**: Handles MCP server connection problems
- **Environment Variables**: Validates required API keys

## 📝 Customization

### Adding New MCP Servers

To add additional MCP servers:

1. Define server parameters in `main.py`:
```python
new_server_params = StdioServerParameters(
    command="your_command",
    args=["your", "args"],
    env={"YOUR_ENV_VAR": os.getenv("YOUR_ENV_VAR")}
)
```

2. Initialize the server connection
3. Add tools to the agent's tool list

### Modifying Image Generation

To customize image generation parameters, edit `image_server.py`:

```python
result = client.images.generate(
    model="dall-e-3",
    prompt=f"Your custom prompt: {query}",
    size="1024x1024",  # Options: 1024x1024, 1792x1024, 1024x1792
    quality="hd",      # Options: standard, hd
    response_format="b64_json"
)
```

### Changing Output Directory

Update the `output_dir` variable in `image_server.py`:

```python
output_dir = "your_custom_directory"
```

## 🔍 Troubleshooting

### Common Issues

1. **Missing API Keys**: Ensure all required environment variables are set
2. **Permission Errors**: Check file system permissions for output directories
3. **Node.js Dependencies**: Verify MCP servers are properly installed
4. **Python Dependencies**: Ensure all required packages are installed

### Debugging

Enable verbose logging by setting:
```python
agent = Agent(
    # ... other parameters
    verbose=True,
)
```

## 📦 Dependencies

### Python Packages
- `crewai`: AI agent framework
- `mcp`: Model Context Protocol client
- `openai`: OpenAI API client
- `httpx`: HTTP client library
- `pydantic`: Data validation

### Node.js Packages
- `@modelcontextprotocol/server-filesystem`
- `@modelcontextprotocol/server-brave-search`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review MCP documentation
3. Open an issue in the repository

## 🔗 Related Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Brave Search API Documentation](https://api.search.brave.com/app/documentation/web-search)

---

**Note**: This project is designed for development and educational purposes. Ensure you comply with all API terms of service and usage limits.
