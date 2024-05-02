import google.generativeai as genai
import json
import strip_markdown


class JobDescriptionParser:
    __GEMINI_PROMPT_MESSAGE = """
        Create a JSON code with just skills, degrees and languages required for this job. Divide skills between hard and soft skills, use only key words for skills and languages. Strictly follow model below:
        {
            "degrees": [],
            "skills": {
                "hard": [],
                "soft": []
            },
            "languages": []
        }
        
        Do not include programming languages inside "languages" key.
        Answer with JSON code only. 
        No other words or observations.
    """

    def __init__(self, geminiApiKey: str):
        genai.configure(api_key=geminiApiKey)
        self.model = genai.GenerativeModel("gemini-pro")

    def parseJobDescription(self, jobDescription: str) -> dict:
        generateContentMessage = f"""
            {self.__GEMINI_PROMPT_MESSAGE}
            {jobDescription}
        """
        response = strip_markdown.strip_markdown(
            self.model.generate_content(generateContentMessage).text
        )
        formattedResponseText = response
        formattedResponseTextLines = formattedResponseText.splitlines()

        print(formattedResponseText)

        if formattedResponseTextLines[0].lower() == "json":
            print("formatting")
            formattedResponseText = formattedResponseText.split("\n", 1)[1]

        return json.loads(formattedResponseText)  # converts string to json
