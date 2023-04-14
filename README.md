# StallmanGPT

StallmanGPT is a Linux command generator and assistant using OpenAI GPT-3.5-turbo. It generates Linux commands based on user input and provides explanations for the generated commands. Users can choose to execute the generated command if it meets their requirements.

## Installation

Install StallmanGPT using pip:

```bash
pip install stallmangpt
```

You will also need an API key for OpenAI. Set the OPENAI_API_KEY environment variable with your OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key
```

## Usage

To use StallmanGPT, run the following command with your desired text as an argument:

```bash
stallmangpt "your desired text"
```

For example:

```bash
stallmangpt "find all .md files and list them"
```

StallmanGPT will generate a Linux command that accomplishes the requested task, provide an explanation of the command, and prompt you to execute the command or not.

## Features

* Generates Linux commands based on user input.
* Provides explanations for the generated commands.
* Allows users to choose whether to execute the generated command or not.
* Implements error handling for OpenAI API usage limits and confidence rating parsing.
* Limits the number of user-initiated retries to 3.

## License

This project is licensed under the MIT License.
