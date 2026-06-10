def execute_agent(question):

    # Lazy import
    from agents.tool_router import route_tool

    return route_tool(question)