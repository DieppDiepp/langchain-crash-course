import pkg_resources

# List of libraries related to LangChain stack
libraries = [
    "langchain",
    "langchain-core",
    "langchain-openai",
    "langchain-community",
    "langchain-experimental",
    "langgraph",
    "langchain-cli",
    "langsmith"
]

# Check and print versions
for lib in libraries:
    try:
        version = pkg_resources.get_distribution(lib).version
        print(f"{lib}=={version}")
    except pkg_resources.DistributionNotFound:
        print(f"{lib} is not installed")
