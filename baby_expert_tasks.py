from crewai import  Task

class BabyExpertTasks():
    def analyze_baby_health(self, user_input, pediatrician_agent):
        return Task(
            description=f"A concerned parent asked: '{user_input}'. As the pediatrician, analyze the baby's health situation in detail, addressing the parent's concern directly. Provide reassurance and guidance on potential steps forward.",
            agent=pediatrician_agent
        )

    def prenatal_and_postnatal_care(self, user_input, obstetrician_agent):
        return Task(
            description=f"Review the query from the parent: '{user_input}'. Offer your expert obstetrical advice on the correct prenatal and postnatal care. Analyze possible implications that the baby's health may have on the mother's well-being. Is really IMPORTANT that you take into account what the pediatrician has said.",
            agent=obstetrician_agent
        )

    def suggest_comforting_activities(self, user_input, child_life_specialist_agent):
        return Task(
            # description="Given the data gathered from pediatrician and obstetrician inputs, suggest activities and behavioral techniques that the parent can engage in with the baby to improve both their emotional health. Make sure your recommendations are concise and effective.",
            description=f"Give your unique perspective on {user_input}. Please take into account what the pediatrician and obstetrician have said.",
            agent=child_life_specialist_agent
        )

    def recommend_developmental_activities(self, user_input, development_specialist_agent):
        return Task(
            # description="In reference to information gathered from previous tasks, recommend activities to optimize the baby's cognitive, social, and emotional growth. Tailor your suggestions based on the specific concerns raised by the parent.",
            description=f"Offer your unique perspective on {user_input}. Please take into account what the pediatrician and obstetrician and child life specialist have said.",
            agent=development_specialist_agent
        )

    def compile_final_guidance(self, user_input, specialist_secretary_agent):
        return Task(
            description=f"Compile the analyses and recommendations from the previous tasks in order to provide a clear answer to the parent's query: '{user_input}'. The final report should answer the parent's concern, provide necessary guidance, and emphasis on the actions to improve the baby's health and development.",
            agent=specialist_secretary_agent
        )