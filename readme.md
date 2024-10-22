# Funny News Generator

This package generates humorous news articles based on real daily news headlines.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/gokbuyuk/FunnyNewsGenerator.git
   cd funny-news-generator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy `config_template.py` to `config.py` and add your OpenAI API key:
   ```
   cp config_template.py config.py
   # Edit config.py and add your API key
   ```

## Usage

Run the application:
```
python run.py
```

Open a web browser and go to `http://localhost:5000` to see your funny news website.

## License

This project is licensed under the MIT License.
