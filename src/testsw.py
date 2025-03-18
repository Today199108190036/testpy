import requests


def get_swagger_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def parse_parameters(parameters, definitions):
    required_params = []
    params_list = []

    for param in parameters:
        param_name = param.get('name')
        param_in = param.get('in')
        param_required = param.get('required', False)
        param_type = param.get('type')
        schema = param.get('schema')

        # 处理schema中的类型或引用
        if schema:
            if '$ref' in schema:
                ref_path = schema['$ref'].split('/')
                model_name = ref_path[-1]
                model = definitions.get(model_name, {})
                model_props = model.get('properties', {})
                model_required = model.get('required', [])

                for prop_name, prop in model_props.items():
                    prop_type = prop.get('type', 'object')
                    if 'items' in prop:
                        prop_type = f"array[{prop['items'].get('type', 'object')}]"
                    params_list.append({
                        'name': prop_name,
                        'type': prop_type,
                        'in': 'body',
                        'required': prop_name in model_required
                    })
                    if prop_name in model_required:
                        required_params.append(prop_name)
            else:
                param_type = schema.get('type', 'object')
                if param_type == 'array':
                    items_type = schema.get('items', {}).get('type', 'object')
                    param_type = f"array[{items_type}]"
        else:
            if param_in in ['query', 'path']:
                if param_required:
                    required_params.append(param_name)
                params_list.append({
                    'name': param_name,
                    'type': param_type or 'string',
                    'in': param_in,
                    'required': param_required
                })

    return required_params, params_list


def extract_api_info(swagger_data):
    api_info = []
    paths = swagger_data.get('paths', {})
    definitions = swagger_data.get('definitions', {})

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']:
                continue

            parameters = details.get('parameters', [])
            required_params, params_details = parse_parameters(parameters, definitions)

            params_result = [{
                'name': p['name'],
                'type': p['type'],
                'in': p['in'],
                'required': p['required']
            } for p in params_details]

            api_info.append({
                'path': path,
                'method': method.upper(),
                'required': required_params,
                'parameters': params_result
            })

    return api_info


def main():
    url = "https://sw.xxx.xxxx.co/xx/xxx-xxx-xxxx-xxxx/v2/api-docs"
    try:
        swagger_data = get_swagger_data(url)
        api_info = extract_api_info(swagger_data)

        for api in api_info:
            print(f"路径: {api['path']}")
            print(f"方法: {api['method']}")
            print("必填参数:", api['required'])
            print("参数列表:")
            for param in api['parameters']:
                print(f"  - 名称: {param['name']}, 类型: {param['type']}, 位置: {param['in']}, 必填: {param['required']}")
            print("\n" + "-" * 50 + "\n")
    except Exception as e:
        print(f"获取或解析API文档时出错: {e}")


if __name__ == "__main__":
    main()