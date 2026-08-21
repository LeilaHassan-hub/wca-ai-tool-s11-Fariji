# Fariji Housing — AI-Powered House Hunting Decision Assistant

## Group Name

**Fariji**

## Group Members

1. **James Gachire** — Admission No. 3640
2. **Zubeda Hassan** — Admission No. 2226
3. **Zipporah Kimani** — Admission No. 3966

## Project Overview

Fariji Housing is an AI-powered decision assistant designed to help house seekers and housing agents simplify the process of finding suitable properties. The tool allows users to enter their housing requirements, such as preferred location, budget, number of bedrooms, property type, and other preferences. The system uses two connected AI API calls to first analyze the user's requirements and then use that analysis to identify and recommend suitable housing options.

## Problem Statement

House hunting can be time-consuming because clients often provide their requirements in natural language, while available property information may contain many different details. Housing agents must interpret these requirements, compare them with available properties, and identify suitable options.

Fariji Housing aims to automate part of this process by analyzing a client's requirements and helping compare available properties. The tool benefits house seekers by providing clearer recommendations and helps housing agents reduce the time spent manually reviewing and comparing properties.

## Tool Description

The tool guides the user through a menu-driven process. The user selects an option and enters their housing requirements.

The first AI stage analyzes the user's input and converts the requirements into structured information. The second AI stage uses the structured requirements together with available property information to evaluate the options and produce a recommendation that the user can act on.

The final recommendation is displayed in a readable format and saved to a file for future reference.

## AI Instruction Design

Both AI calls will use the **R-T-C-C-O framework**:

- **Role** — Defines the role the AI should perform.
- **Task** — States what the AI must accomplish.
- **Context** — Provides the information required by the AI.
- **Constraints** — Defines the rules and limitations the AI must follow.
- **Output Format** — Specifies how the AI should structure its response.

### Stage 1 — Requirements Analysis

The first AI instruction will direct the model to analyze the user's housing requirements and identify important details such as location, budget, bedrooms, property type, and preferences.

The response will be requested in JSON format so that Python can parse the information and pass the results to the second AI stage.

### Stage 2 — Property Decision

The second AI instruction will use the structured requirements produced by Stage 1 together with the available property information. It will compare the options, identify suitable properties, explain the strongest match, and provide a practical recommendation.

## Technical Overview

The tool will be developed in Python and connected to an AI model through an API.
