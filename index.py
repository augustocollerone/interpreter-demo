from interpreter import interpreter

# interpreter.llm.api_base = "https://17bb-181-171-24-111.ngrok-free.app/v1"
# interpreter.llm.api_key = "fake_key"
# interpreter.llm.model = "mistral/mistral-small"

interpreter.llm.api_key = "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"

# interpreter.custom_instructions = "Whenever you need to use a web browser don't use computer.browser, instead use import webbrowser"

# interpreter.computer.offline = False
# interpreter.computer.verbose = True
# interpreter.computer.emit_images = True

interpreter.anonymous_telemetry = False
interpreter.os = True

interpreter.chat()