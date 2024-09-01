const fs = require('fs');

function interpret(code) {
  const lines = code.split('\n');

  lines.forEach(line => {
    line = line.trim();

    if (line.startsWith('import')) {
      const module = line.match(/import\("(.+)"\)/)[1];
      console.log(`# Importando módulo ${module}`);
    } else if (line.startsWith('tryto')) {
      const script = line.match(/tryto\(open\("(.+)"\)/)[1];
      const errorMsg = line.match(/error\(all, \{(.+)\}\)/)[1];
      console.log(`try:`);
      console.log(`    with open("${script}") as file:`);
      console.log(`        # Executar script`);
      console.log(`except Exception as e:`);
      console.log(`    print("${errorMsg}")`);
    } else if (line.startsWith('screentext')) {
      const text = line.match(/screentext\("(.+)"\)/)[1];
      console.log(`print("${text}")`);
    } else if (line.match(/var\s+\w+\s*=\s*\d+/)) {
      const [varName, value] = line.split('=').map(s => s.trim());
      console.log(`${varName} = ${value}`);
    } else if (line.match(/var\s+\w+\s*=\s*\{.+\}/)) {
      const [varName, content] = line.split('=', 2).map(s => s.trim());
      console.log(`${varName} = {${content}}`);
    } else if (line.match(/var\s+\w+\s*=\s*\[.+\]/)) {
      const [varName, content] = line.split('=', 2).map(s => s.trim());
      console.log(`${varName} = [${content}]`);
    }
  });
}

const code = fs.readFileSync('example.psr', 'utf8');
interpret(code);
