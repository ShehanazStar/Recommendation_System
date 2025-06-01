import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
API_KEY = "AIzaSyA-9-lTQTWdNM43YdOXMQwGKDy0SrMwo6c"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Core Modules of the LLM Agent
class LLMAgent:
    def __init__(self, model):
        self.model = model
        self.memory = []  # Simulate long-term memory for user preferences and history

    # Perception Module: Process user input
    def perceive(self, user_input):
        return user_input

    # Control Module: Plan and decompose tasks
    def plan(self, task):
        prompt = f"Break down the task '{task}' into smaller sub-tasks. Provide a numbered list."
        response = self.model.generate_content(prompt)
        return response.text

    # Action Module: Execute tasks using external tools or APIs
    def act(self, sub_tasks):
        results = []
        for sub_task in sub_tasks.split("\n"):
            if sub_task.strip():  # Ignore empty lines
                prompt = f"Perform the task: {sub_task}"
                response = self.model.generate_content(prompt)
                results.append(response.text)
        return results

    # User Simulation: Simulate user feedback
    def simulate_user_feedback(self, results):
        feedback_prompt = f"Based on these results: {results}, provide constructive feedback."
        feedback = self.model.generate_content(feedback_prompt)
        return feedback.text

    # Memory Management: Store and retrieve information
    def update_memory(self, new_info):
        self.memory.append(new_info)

    def retrieve_memory(self):
        return self.memory

# Streamlit App
def main():
    st.title("LLM Agent for Recommendation and Search Systems")
    st.write("This app demonstrates an LLM agent for recommendation and search tasks, inspired by the survey paper.")

    # Initialize the LLM agent
    agent = LLMAgent(model)

    # Sidebar for memory management
    st.sidebar.header("Memory Management")
    if st.sidebar.button("View Memory"):
        memory = agent.retrieve_memory()
        st.sidebar.write("Agent Memory:")
        for item in memory:
            st.sidebar.write(f"- {item}")

    # Main app functionality
    st.header("Choose a System")
    system_choice = st.radio("Select a system:", ("Recommendation System", "Search System"))

    if system_choice == "Recommendation System":
        st.subheader("Recommendation System")
        user_input = st.text_input("Enter your request (e.g., 'Recommend a good Italian restaurant in New York'):")

        if st.button("Get Recommendation"):
            if user_input:
                # Step 1: Perceive user input
                perceived_input = agent.perceive(user_input)

                # Step 2: Plan and decompose the task
                task_plan = agent.plan(perceived_input)
                st.write("Task Plan:")
                st.write(task_plan)

                # Step 3: Execute sub-tasks
                results = agent.act(task_plan)
                st.write("Results:")
                for result in results:
                    st.write(result)

                # Step 4: Simulate user feedback
                feedback = agent.simulate_user_feedback(results)
                st.write("User Feedback:")
                st.write(feedback)

                # Step 5: Update memory with user preferences
                agent.update_memory(f"User requested: {user_input}")
            else:
                st.warning("Please enter a request.")

    elif system_choice == "Search System":
        st.subheader("Search System")
        user_input = st.text_input("Enter your query (e.g., 'What are the benefits of using large language models in recommendation systems?'):")

        if st.button("Search"):
            if user_input:
                # Step 1: Perceive user input
                perceived_input = agent.perceive(user_input)

                # Step 2: Plan and decompose the task
                task_plan = agent.plan(perceived_input)
                st.write("Task Plan:")
                st.write(task_plan)

                # Step 3: Execute sub-tasks
                results = agent.act(task_plan)
                st.write("Results:")
                for result in results:
                    st.write(result)

                # Step 4: Simulate user feedback
                feedback = agent.simulate_user_feedback(results)
                st.write("User Feedback:")
                st.write(feedback)

                # Step 5: Update memory with search context
                agent.update_memory(f"User searched for: {user_input}")
            else:
                st.warning("Please enter a query.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
