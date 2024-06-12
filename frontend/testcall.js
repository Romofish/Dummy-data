// 获取并显示output数据集
fetch('http://localhost:5000/api/output')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // can choose the output format
    })
    .catch(error => console.error('Error:', error));

// 更新output数据集
function updateOutput(newOutput) {
    fetch('http://localhost:5000/api/output', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newOutput)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

// 获取特定domain的配置
function getDomainConfig(domain) {
    fetch(`http://localhost:5000/api/config/${domain}`)
        .then(response => response.json())
        .then(config => console.log(config))
        .catch(error => console.error('Error:', error));
}

// 更新特定domain和变量的配置
function updateDomainVariableConfig(domain, variable, newConfig) {
    fetch(`http://localhost:5000/api/config/${domain}/${variable}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newConfig)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

// 示例使用
const domain = 'AE';
const variable = 'STUDYID';
const newConfig = {
    "Variable Label": "Study Identifier",
    "Type": "Char",
    "Controlled Terms, Codelist or Format": ["New Term 1", "New Term 2"],
    "Core": "Req",
    "Order": 1.0
};

getDomainConfig(domain);
updateDomainVariableConfig(domain, variable, newConfig);

// 示例更新output数据集(开不开还没决定，数据示例如下)
const newOutput = {
    "items": [
        {
            "id": 1,
            "name": "Item 1",
            "configurable_field": "updated value 1"
        },
        {
            "id": 2,
            "name": "Item 2",
            "configurable_field": "updated value 2"
        }
    ]
};
updateOutput(newOutput);
