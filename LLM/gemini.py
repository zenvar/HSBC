"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

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
    system_instruction="以下是一段关于HSBC汇丰银行科技部门相关岗位的描述，需要总结整理输出为指定格式，语言为中文，力求简洁且抓住重点，直接输出Markdown格式结果。\n预期输出结果需要保留岗位核心信息，且保持简洁明了。\n预期输出结果格式可以随机选择以下几种参考样式之一，也可适当自由发挥：\n如参考一：\n🆔** 岗位ID **: 0000KNYO  \n📍** 工作地点 **: 广州  \n📅**开放时段**: 2024.10.4 - 2024.10.18  \n🏢** 业务部门 **: 市场与证券服务技术 (Markets & Sec Services Tech)  【注意：只需这几种基础信息即可】  \n\n🧑‍💻** 职责概述 *:       【注意：这部分职责业务简短一两句话概述即可，但岗位title保留原文英文以及对应中文翻译】  \nSenior Consultant Specialist（高级咨询专家）岗位主要负责汇丰银行全球FX计算团队的交易后风险和PnL计算解决方案平台的开发、改进和维护。  \n🌟** 岗位要求**：【强调硬性条件、技术栈、加分项等岗位重点，使用一段话总结而非列表列举】  \n候选人拥有8年以上Java后端开发经验，熟悉微服务、消息队列、云服务 ( GCP)、前端、Agile、CI/CD等技术，并具备扎实的SQL技能和高可用性、No-SQL 或列式数据库。  \n⭐**加分项**：【如果岗位有加分或者偏好点需要着重列举】  \n熟悉PostgreSQL数据库优先、高性能和可扩展性设计经验，对金融投资产品（特别是FX）的交易生命周期和交易后处理知识有了解者更佳。 同时，需要有领导或负责交付复杂Java服务/模块的经验，以及流利中英文沟通能力和分析问题能力。  \n📬 [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/xxx......)  \n\n以及参考二：  \n🆔**岗位ID**: 0000KJWP  \n📍**工作地点**: 西安  \n📅**开放时段**: 2024.09.08 - 2024.10.27  \n🏢**业务部门**: 财富与个人银行业务IT (Wealth Personal Banking IT 基于Job Description中的WPB推断)  \n\n\n🧩**职责概述**:  \nLead Consultant Specialist（首席高级咨询专家）负责科技交付全生命周期，包括产品或服务的启动、构建、测试、发布和持续维护。  需与工程师、架构师和业务利益相关者合作，确定并开发最合适的技术解决方案。  \n\n🎯** 岗位要求 **:  \n🥇** 硬性要求 **: 全栈软件工程能力(前端、中间件、后端)，熟悉最新技术，拥有金融服务行业业务知识，能够阅读最新的学术和研究论文；8-10年以上工作经验(本科毕业后)，硕士或博士学历优先，国际顶尖大学毕业生更佳；具备在DevOps环境和敏捷团队中工作的经验。  \n🥈**技术栈**: 熟悉微服务、容器化，至少一个云平台(AWS, GCP, Azure, 阿里云)的实际项目经验，精通至少两种编程语言(Java/Python/Golang/Node.js)，熟悉相关设计模式和数据库(关系型数据库和NoSQL数据库)，能够使用和扩展常用开源框架(Spring, TensorFlow, Ethereum等)。  \n🥉**加分项**:  国际学术界/工业界/开源社区贡献经验；大型语言模型(GPT/Llama/Bard)项目经验(6个月以上)；精益创业方法论和VC风格投资组合管理经验；孵化器、加速器、风投公司和初创企业生态系统知识；大型企业环境中交付数字产品经验。  \n\n📮 [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/xxx......)  \n\n\n以及参考三：  \n🆔**岗位ID**: 0000KOBS  \n📍**工作地点**: 广州  \n📅**开放时段**: 2024.10.04 - 2025.12.31  \n🏢**业务部门**: 区域CIO - 亚太地区 (Regional CIO - ASP)  \n\n📖**职责概述**:  \nSenior Consultant Specialist（高级咨询专家）负责支持亚太地区国家业务和IT团队，参与开发项目的全生命周期，主要维护iSeries平台及一些小型应用程序。  需要经常出差至马来西亚、印度尼西亚、澳大利亚等国家，与当地团队紧密合作。  \n\n🎯**岗位要求**:  \n必须具备6-12年AS400 RPG软件开发经验，熟悉AS400、RPGLE、CL on iSeries， 拥有HUB、ATMP、HSS、HIE、TREATS项目经验者优先。需要具备软件技术设计、编码和测试经验，能够独立工作，高效处理压力下的紧迫任务，并具备良好的分析和解决问题能力。  熟悉Agile/DevOps方法和实践，熟悉Jira、RTC、ARCAD、Jenkins等DevOps工具者优先。  \n\n✈️**特殊要求**:  需要频繁出差至亚太地区国家，具备良好的英语沟通能力，并能适应弹性工作制（包括周末和加班）。  \n\n📧 [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/xxx......)  \n以及：  \n🆔**岗位ID**: 0000KAZH  \n🗺️**工作地点**: 广州  \n📅**开放时段**: 2024.10.04 - 2024.12.03  \n🏢**业务部门**: 集团数据技术 (Group Data Technology)  \n\n🧑‍💼**职责概述**:  \nTransformation Project Manager（转型项目经理）负责管理汇丰银行的数字化转型项目，涵盖项目生命周期的规划、执行、监控和控制。  \n\n🎯**岗位要求**:  \n具备跨国/地区项目管理经验，熟悉金融行业，拥有卓越的沟通能力、关系管理能力和敏锐的洞察力。需具备扎实的项目管理经验，熟悉多种项目管理方法论（例如Agile），能够有效与不同利益相关方协作。  流利的中英文（及粤语）沟通能力是必须的。  \n\n✨**加分项**:  \nPMP、MSP、Prince 2或Agile PM等项目管理认证；ACIB等本地银行资格证书；设计与启动（D&I）变革经验。  \n💌 [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/xxx......)  \n\n【注：输出结果可适当增加emoji符号增加排版可读，符合语境即可，不指定以上这几种。Markdown标签起强调作用。希望排版可以自由发挥】",

    )

    chat_session = model.start_chat(
        history=[
            {
      "role": "user",
      "parts": [
        "根据系统指令，模拟输出一个样例",
      ],
    },
    {
      "role": "model",
      "parts": [
        "🆔 ** 职位ID **: 0000KN4X  \n🌏 ** 地点 **: 广州  \n⏰ ** 申请时间 **: 2024年9月23日 - 2024年10月7日  \n🏢 ** 业务部门 **: 市场与证券服务技术 (Markets & Sec Services Tech)  \n\n ** 🧑‍💻职位概述 **:  \nBanks and Broker Dealers Chief Engineer（银行和经纪商首席工程师）将负责推动BBD领域的工程最佳实践，建立和完善标准化工具，协助平台负责人解决技术难题，推动技术重用，促进团队整体技术能力提升。  \n\n **📖岗位要求**:  \n具备出色的沟通与领导力，能够独立工作，并为团队提供技术方向。精通CI/CD流程、软件开发、API设计、测试、以及可靠性工程，具备架构设计与安全编码的丰富经验。擅长探索新技术并推动实践，能够在跨领域解决多种技术问题，支持团队合作和技能提升。  \n\n📮 **申请链接**: [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/Banks-and-Broker-Dealers-Chief-Engineer/245077)",
      ],
      
    },{
      "role": "user",
      "parts": [
        "根据系统指令，参考样式二模拟输出一个样例",
      ],
    },
    {
      "role": "model",
      "parts": [
        "🆔 **岗位ID**: 0000KJ99  \n📌 ** 工作地点 **: 上海  \n📅 ** 开放时段 **: 2024.10.20 - 2024.11.10  \n🏢 ** 业务部门 **:  全球银行与市场业务IT (Global Banking and Markets IT)  \n\n\n⚙️** 职责概述 **:  \nSenior Software Engineer (高级软件工程师) 负责设计、开发和维护汇丰银行全球银行和市场业务的关键交易系统。  需要与业务分析师、架构师和其他工程师紧密合作，确保系统的高性能、可扩展性和安全性。  \n\n\n🛠️ **岗位要求**:  \n🥇**硬性要求**: 5年以上软件开发经验，精通Java或C++编程语言，熟悉面向对象设计原则，具备良好的问题解决能力和沟通能力。熟悉金融行业知识优先。  \n🥈**技术栈**:  熟练掌握Spring Boot, Microservices, RESTful APIs, SQL, NoSQL数据库(例如MongoDB, Cassandra)，熟悉Docker和Kubernetes等容器化技术，以及CI/CD流程。  \n🥉**加分项**:  拥有大型分布式系统开发经验；熟悉云平台(AWS, Azure, GCP)；对高频交易系统有了解；具备Agile开发经验。  \n\n\n💌 [投递简历](https://mycareer.hsbc.com/en_GB/external/PipelineDetail/xxx......)  \n",
      ],
    },{
      "role": "user",
      "parts": [
        "接下来我会提供岗位描述原文信息，你根据系统指令格式，输出总结",
      ],
    },
    {
      "role": "model",
      "parts": [
          "好的，我将会严格根据系统指令要求与格式，根据岗位描述情况与排版安排，合理的选择一种样式，也会适当自由发挥。"
      ],
    },
    
      ]
    )
    return chat_session.send_message(JD).text
