Build a keynote writing agent using CrewAI and watsonx.ai(IBM AI Cloud Platform).

# Explanation 

The code is a setup for running multiple agents (in this case 2 agents) using IBM Watsonx LLM models and tools like Serper for web search. The first agent ("researcher") is tasked with finding examples of AI research using the Serper tool while the second agent ("writer") uses the research to generate an engaging keynote speech. Both tasks are managed by a crew (multiagent orchestration framework), with each agent focusing on its specific goal, and the results are saved in output files.

# Startup 
1. Clone the repo `git clone `
2. Install initial deps `pip install -r requirements.txt`
3. Replace the Serper Dev API key with your own from https://serper.dev/api-key
4. Replace the watsonx.ai API with your own from https://cloud.ibm.com/iam/apikeys
5. Replace the project id with a watsonx.ai project id 
6. Run the flow `python agent.py`


Author: Khalil Bezrati 

