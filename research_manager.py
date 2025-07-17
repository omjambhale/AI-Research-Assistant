from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
from clarifier_agent import clarifier_agent, ClarificationData
import asyncio

class ResearchManager:

    async def generate_clarifying_questions(self, query: str) -> ClarificationData:
        """ Generate clarifying questions based on the query """
        print("Generating clarifying questions...")
        result = await Runner.run(
            clarifier_agent,
            f"Query: {query}",
        )
        clarification_data = result.final_output_as(ClarificationData)
        print(f"Generated {len(clarification_data.questions)} clarifying questions")
        return clarification_data

    async def run_with_clarification(self, query: str, clarifying_answers: list[str]):
        """ Run the deep research process with clarifying questions, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research with clarifications...")
            
            # Plan searches using clarifications
            search_plan = await self.plan_searches(query, clarifying_answers)
            yield "Searches planned, starting to search..."     
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."
            report = await self.write_report(query, clarifying_answers, search_results)
            yield "Report complete!"
            yield report.markdown_report

    async def plan_searches(self, query: str, clarifying_answers: list[str]) -> WebSearchPlan:
        """ Plan the searches to perform for the query using clarifying answers """
        print("Planning searches with clarifications...")
        input_text = f"Query: {query}\nClarifying answers: {clarifying_answers}"
        result = await Runner.run(
            planner_agent,
            input_text,
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Perform the searches to perform for the query """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results

    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for the query """
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def write_report(self, query: str, clarifying_answers: list[str], search_results: list[str]) -> ReportData:
        """ Write the report for the query """
        print("Thinking about report...")
        input = f"Original query: {query}\nClarifying answers: {clarifying_answers}\nSummarized search results: {search_results}"
        result = await Runner.run(
            writer_agent,
            input,
        )
        print("Finished writing report")
        return result.final_output_as(ReportData) 