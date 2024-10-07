"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from config.Config import Config

config = Config()

genai.configure(api_key= config.get('gemini','key'))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
  "response_mime_type": "text/plain",
}




def GeminiSummary(JD):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="以下是一段关于HSBC汇丰银行科技部门相关岗位的描述，需要总结整理输出为指定格式，语言为中文，力求简洁且抓住重点，在Markdown的代码块中输出结果。\n预期输出结果需要保留岗位核心信息，如基础信息：岗位Title，地址，开放时间段，业务部门（岗位描述的business 字段一般有说明，HSBC内部业务有如Wealth and Personal Banking ，Markets and Securities Service等）；除了基础信息外，内容主体也需要用简短一两段话，几句以内（250字左右为宜）总结描述该岗位职责与要求，并且需要遵循以下原则，灵活保留该岗位最核心最特别的要求：其中职责描述应该一两句话简短介绍即可，不要过于详细的介绍具体业务。优先保留突出岗位核心要点，如硬性要求（学历、经验年限等），技术栈，加分项偏好等特殊要求；对一些所有岗位适用的如沟通能力、团队合作等车轱辘话不必突出，但可根据岗位类型考虑（如高级技术管理岗会比单纯的初级技术岗位对软实力要求更多，也有对流利英语国语粤语有高要求，也可能需要外国出差等）。输出结果可适当增加emoji增加排版可读性、markdown标签起强调作用。\n如预期输出结果为：\n```\n🆔岗位ID: 0000KNYO\n📍工作地点: 广州\n📅开放时段: 2024.10.4 - 2024.10.18\n🏢业务部门: Markets & Sec Services Tech  【注：emoji符号符合语境即可，不指定一定是这几种】\n\n📖职责概述:       【注意：这部分职责业务简短一两句话概述即可，但岗位title保留原文英文以及对应中文翻译】\nSenior Consultant Specialist（高级咨询专家）岗位主要负责汇丰银行全球FX计算团队的交易后风险和PnL计算解决方案平台的开发、改进和维护。\n☑️岗位要求：【强调硬性条件、技术栈、加分项等岗位重点】\n候选人拥有8年以上Java后端开发经验，熟悉微服务、消息队列、云服务 ( GCP)、前端、Agile、CI/CD等技术，并具备扎实的SQL技能和高可用性、No-SQL 或列式数据库。\n ❤️加分项：\n熟悉PostgreSQL数据库优先、高性能和可扩展性设计经验，对金融投资产品（特别是FX）的交易生命周期和交易后处理知识有了解者更佳。 同时，需要有领导或负责交付复杂Java服务/模块的经验，以及流利中英文沟通能力和分析问题能力。  \n\n```\n\n以及：\n```\n岗位ID: 0000KAZH\n工作地点: 广州\n开放时间段: 2024.10.4 - 2024.12.3\n业务部门: Technology\n\n职责概述:\nTransformation Project Manager(转型项目经理)负责管理HSBC的数字化转型项目，包括规划、执行、监控和控制项目生命周期。\n\n要求候选人具备相关的跨国/地区项目管理经验、金融行业理解以及高沟通能力、关系管理能力以及敏锐的洞察力。需要扎实的项目管理经验，熟悉多种项目管理方法论 (例如 Agile)，并能够有效地与不同利益相关方协作。\n 流利的中英文（与粤语）是必须的。加分项包括：PMP、MSP、Prince 2 或 Agile PM 等项目管理认证，以及ACIB等本地银行资格证书、设计与启动（D&I）变革经验。\n```\n\n以及：\n```\n岗位ID: 0000KOBS\n工作地点: 广州\n开放时间段: 2024.10.4 - 2025.12.31\n业务部门: Regional CIO - ASP\n\n职责概述:\nSenior Consultant Specialist(高级咨询专家)负责与本地管理层合作，支持亚洲太平洋地区 (ASP) 国家业务和 IT 团队，参与开发项目的各个阶段。主要支援 iSeries 平台，也有一些本地小型应用程序。岗位要求需经常出差到ASP地区国家，例如马来西亚、印度尼西亚和澳大利亚，了解当地的业务重点，并与当地 IT 团队密切合作。\n \n要求候选人拥有 6-12 年 AS400 RPG 软件开发经验，优先考虑 HUB、ATMP、HSS、HIE、TREATS 项目经验。需要有软件技术设计、编码和测试经验，并具备分析和解决问题的能力，可以独立工作，并能在压力下紧迫的时限内高效工作。  需熟练掌握 AS400 、RPGLE、CL on iSeries，熟悉 Agile/DevOps 方法和实践，熟悉 DevOps 工具（如 JIRA、RTC、ARCAD、Jenkins 等）将更有加分项。此外，还需要积极主动、适应变化，拥有良好的沟通表达能力和良好的英语书面和口语能力，并准备好配合工作需求进行离岸工作和出差，具备周末和加班的弹性工作能力。\n```\n以及：\n```\n岗位ID: 0000KNS9\n工作地点: 广州/西安\n开放时间段: 2024-09-27 - 2024-10-11\n业务部门: Wealth Personal Banking IT\n\n职责概述:\nSenior Lead Consultant Specialist（首席高级咨询专家）负责科技交付全生命周期内的所有阶段，包括启动、架构、测试、发布和持续维护产品或服务。 \n\n要求候选人拥有全栈软件开发能力，熟悉最新技术，并在银行金融服务领域拥有业务知识。同时，需要具备优秀的分析、设计和解决问题能力，以及良好的团队合作精神和沟通能力。偏向硕士或博士学历以及国际顶尖大学毕业生。\n\n❤️加分项: \n* 国际学术界、工业界、开源项目贡献；\n* 具备大型语言模型 (例如 GPT / Llama / Bard) 相关的项目经验\n* 熟练使用至少一云平台 (AWS, GCP, Azure 或 Ali Cloud) 进行可扩展解决方案构建经验\n* 具备 Lean Startup 方法论和 VC 投资管理经验； \n* 了解孵化器、加速器、风险投资公司和初创企业生态系统；\n* 在大型企业环境中交付数字产品经验。      \n\n```",

    )

    chat_session = model.start_chat(
        history=[
      ]
    )
    return chat_session.send_message(JD).text
