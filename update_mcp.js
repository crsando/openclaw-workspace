const fs = require('fs');
const path = require('path');

const configPath = path.join(process.env.HOME, '.openclaw', 'openclaw.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

config.mcpServers = config.mcpServers || {};
config.mcpServers.jin10 = {
  serverUrl: "https://mcp.jin10.com/mcp",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-eRwpa6OAlEHhRt_ZBDpoJizXWzcYunEWALi4NuyI8YA"
  }
};

fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
console.log('Successfully updated MCP config');
