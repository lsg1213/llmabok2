from pydantic import BaseModel, Field

class CountryInput(BaseModel):
    country: str = Field(description="The country to get information about.")

class CapitalInfoOutput(BaseModel):
    country: str = Field(description="The country to get information about.")
    capital: str = Field(description="The capital city of the country.")

from google.adk.agents import Agent

root_agent = Agent(
    name="country_agent",
    model="gemini-2.0-flash",
    input_schema=CountryInput,
    output_schema=CapitalInfoOutput,
    instruction=f"당신은 수도 정보를 제공하는 에이전트입니다. 다음 형식에 맞춰서 출력해주세요. \
                {CapitalInfoOutput.model_json_schema()}",
    output_key="output",
    include_contents='none',
    # description="""너는 국가에 대한 정보를 제공하는 전문가야. 주어진 국가의 수도를 알려줘.
    # 사용자가 입력한 국가에 대한 수도 정보를 알려줘.
    # 만약 국가를 모르면 '몰루'라고 답변해줘.
    # 입력 예시: {"국가": "대한민국"}
    # 출력 예시: {"수도": "서울"}""",
)
print(CountryInput.model_json_schema())
