# -*- coding: utf-8 -*-
from openai import OpenAI

client = OpenAI(api_key="sk-8032b28d2ea84d39b5aa8b9a48572897", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个专业的软件测试工程师"},
        {"role": "user", "content": "请根据以下接口定义生成完整的测试用例：\n\n路径: /api/msg-admin/application/create\n方法: POST\n参数列表:\n  - 名称: id, 类型: integer, 位置: body, 必填: False\n  - 名称: name, 类型: string, 位置: body, 必填: False\n  - 名称: remark, 类型: string, 位置: body, 必填: False\n\n请按以下要求输出测试用例：\n1. 测试用例字段完整，至少包含用例编号、用例名称、前置条件、测试步骤、预期结果。\n2. 考虑到需求中涉及的关键点和风险点。\n3. 测试用例全面覆盖所有功能点、边界条件、等价类、状态变化和输入组合。\n4. 保留所有关键信息，包括判断条件、具体的数值、必填和非必填字段。\n5. 只需要编写功能测试用例。\n6. 忽略逻辑不合理或结果不确定的特殊测试用例。"},
    ],
    stream=False
)

print(response.choices[0].message.content)