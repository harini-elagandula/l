from multi_ai_finance.venv.backend.agents import finance_agent

query = input("Enter your financial details: ")

response = finance_agent.run(query)

print("\n--- AI Financial Analysis ---\n")
print(response.content)