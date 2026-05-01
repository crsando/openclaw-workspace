const fs = require('fs');
const path = require('path');

const configPath = path.join(process.env.HOME, '.openclaw', 'openclaw.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

delete config.mcpServers;

fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
console.log('Reverted invalid MCP config');
