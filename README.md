# Fariji Housing — AI-Powered House Hunting Decision Assistant

## Group Name

**Fariji**

## Group Members

1. **James Gachire** — Admission No. 3640
2. **Zubeda Hassan** — Admission No. 2226
3. **Zipporah Kimani** — Admission No. 3966

## Project Overview

Fariji Housing is an AI-powered decision assistant that helps clients find suitable houses in **Kasarani, Nairobi**.

The user describes what they need, such as house type and budget. The tool uses **two connected AI API calls**:

1. **Stage 1:** Analyses the client's housing requirements.
2. **Stage 2:** Uses the analysis to recommend a suitable property.

The final recommendation is displayed and saved to a file.

## Problem Statement

Finding a suitable house can take time because clients describe their needs in different ways. It can also be difficult to compare house types, rents, and features.

Fariji Housing helps simplify this process by understanding the client's request and recommending a suitable house from the available properties.

## Target Users

* People looking for houses in Kasarani.
* Housing agents who want to quickly identify suitable options for clients.

## Location

The Fariji Housing knowledge base focuses on **Kasarani, Nairobi ONLY**.

All properties have:

* Individual electric meters
* Individual water bills
* Security
* Different rental prices depending on the house type

## Available House Types

| House Type  |            Rent |
| ----------- | --------------: |
| 2 Bedroom   | From KSh 40,000 |
| 1 Bedroom   | From KSh 25,000 |
| Bedsitter   | From KSh 12,000 |
| Single Room |  From KSh 4,500 |
| Single Room |       KSh 6,000 |

## How the Tool Works

The user can start with a normal message such as:

> Hello

The assistant responds politely and briefly explains that it helps users find houses in Kasarani.

The user can then describe their requirements in their own words, for example:

> I need a 2 bedroom house in Kasarani with a budget of 40,000.

The system processes the request and provides a suitable recommendation.

## Two-Stage AI Process

### Stage 1 — Requirements Analysis

The first AI call analyses the client's message.

It identifies information such as:

* House type
* Budget
* Requirements
* Missing information

The response is requested in **JSON format** so that Python can safely process it.

### Stage 2 — Property Decision

The second AI call receives the Stage 1 result and the available property information.

It then:

* Compares the client's requirements with available properties.
* Finds a suitable option.
* Explains the recommendation.
* Avoids inventing property information.

The second API call therefore uses the result of the first API call.

## AI Instruction Design — R-T-C-C-O

The R-T-C-C-O structure is used consistently across both AI stages. Stage 1 uses the framework to analyse the client's requirements, while Stage 2 uses it to produce a property recommendation based on the analysed requirements and the available knowledge base.

Both AI prompts follow the **R-T-C-C-O framework**.

### 1. Role

Defines what role the AI should perform.

Example:

> You are Fariji Housing Assistant.

### 2. Task

Explains what the AI needs to do.

Example:

> Analyse the client's housing request and identify their requirements.

### 3. Context

Provides the information needed by the AI.

This includes the Kasarani location and available house information.

### 4. Constraints

Sets rules for the AI.

Examples:

* Recommend properties in Kasarani only.
* Do not invent property details.
* Use the available knowledge base.
* Keep the response clear and useful.

### 5. Output Format

Defines how the AI should respond.

Stage 1 uses **JSON** so Python can parse the result. Stage 2 produces a simple recommendation that the client can understand.

## Technical Overview

The tool is developed using **Python** and connects to an AI model through the **OpenAI API**.

Main technologies:

* Python
* OpenAI API
* JSON
* python-dotenv
* `.env` environment variables

The API key is stored in `.env` and is **not written directly in the Python code**.

The program uses `try/except` to handle errors such as:

* Empty input
* API failure
* Invalid JSON response

The final result is saved to a text file so that the user keeps a copy after the program closes.

## JSON Handling

Stage 1 requests a JSON response containing information such as:

```json
{
    "property_type": "2 bedroom",
    "budget": "40000",
    "needs_more_information": false,
    "message": ""
}
```

Python parses this JSON and sends the information to Stage 2.

## Saved Output

The final recommendation is saved in:

```text
fariji_result.txt
```

The saved file contains:

* Client request
* Stage 1 analysis
* Final recommendation

## Error Handling

The program is designed not to crash when common problems occur.

It handles:

* Empty user input
* Missing API key
* Failed API requests
* Invalid JSON responses
* Other unexpected errors

The user receives a clear message instead of the program suddenly closing.

## Security

The OpenAI API key is stored in a `.env` file.

The `.env` file is included in `.gitignore` so that the API key is not uploaded to GitHub.

**The API key must never be committed to the repository.**

## GitHub Collaboration

The project is maintained in a shared GitHub repository.

Each group member is expected to make at least **3 meaningful commits**, as required by the project instructions.

Commit messages should clearly describe the work completed, for example:

```text
Add Stage 1 requirements analysis
Add second API recommendation stage
Improve error handling
```

## Division of Roles

### James Gachire — Python & API Integration

Responsibilities:

* Set up the Python project.
* Connect the project to the OpenAI API.
* Implement the two API calls.
* Test API integration.
* Make at least 3 meaningful GitHub commits.

### Zubeda Hassan — Knowledge Base & Testing

Responsibilities:

* Prepare and maintain the housing knowledge base.
* Check property types, rents, and features.
* Test different client requests.
* Test invalid and empty input.
* Help document testing and error handling.
* Make at least 3 meaningful GitHub commits.

### Zipporah Kimani — Prompts, Documentation & Presentation

Responsibilities:

* Design and document the R-T-C-C-O prompts.
* Help improve the user-facing responses.
* Prepare the README and project documentation.
* Help prepare the live demonstration and presentation.
* Make at least 3 meaningful GitHub commits.

## Project Requirements Checklist

* [x] Python script
* [x] Two connected AI API calls
* [x] Stage 2 uses Stage 1 results
* [x] R-T-C-C-O prompt design
* [x] JSON handling
* [x] User input
* [x] Saved output file
* [x] Error handling
* [x] API key stored securely in `.env`
* [x] `.gitignore`
* [x] GitHub collaboration
* [x] README documentation

These requirements follow the course project specification, which requires a working Python tool, two connected API requests, R-T-C-C-O prompts, JSON handling, saved output, error handling, and secure API-key storage.

## How to Run
The following explains how to install, configure, and run Fariji Housing

### 1. Install Python

Make sure Python is installed.

### 2. Install the required packages

```bash
pip install openai python-dotenv
```

### 3. Create the `.env` file

Add:

```env
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the program

```bash
python main.py
```

### 5. Describe the house you need

For example:

```text
I need a 2 bedroom house in Kasarani with a budget of 40000.
```

The assistant analyses the request and provides a recommendation.

## Ethics and Responsible AI

Fariji Housing should provide recommendations responsibly.

The tool should:

* Use only the available housing information.
* Avoid inventing property details.
* Be clear when information is missing.
* Protect the API key.
* Avoid collecting unnecessary personal information.
* Make it clear that the AI recommendation does not replace the client's final decision.

## Testing

The group will test:

1. A normal housing request.
2. A greeting such as "Hello".
3. Different house types.
4. Different budgets.
5. Empty input.
6. Invalid or incomplete requests.
7. API failure.
8. Invalid JSON.
9. Correct saving of the final result.

## Future Improvements

With more time, the group could add:

* More Kasarani properties.
* More detailed property information.
* Better budget matching.
* Property comparison.
* A simple graphical interface.
* More advanced filtering.

## Conclusion

Fariji Housing is a simple AI-powered decision assistant designed for house hunting in Kasarani, Nairobi. It uses two connected AI stages to understand client requirements and provide useful housing recommendations. The project demonstrates AI integration, prompt design, JSON processing, Python programming, error handling, secure API-key management, and GitHub collaboration.
