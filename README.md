# church-mcp
<!-- mcp-name: io.github.gabrielmahia/church-mcp -->

## Why This Exists

Faith institutions run a substantial share of Kenya's schools, clinics and welfare programmes, but their service directories are fragmented by denomination. For someone seeking help, the relevant question is what is nearby and open, not who runs it.

## Install

```bash
pip install church-mcp
```

## Tools (6)

- **`catholic_diocese_finder`** —   
  <sub>args: county</sub>
- **`protestant_denomination_guide`** —   
  <sub>args: no arguments</sub>
- **`muslim_community_guide`** — Return Muslim community organisations, mosques, and welfare services in Kenya.  
  <sub>args: county</sub>
- **`religious_community_services`** —   
  <sub>args: no arguments</sub>
- **`church_legal_registration`** —   
  <sub>args: no arguments</sub>
- **`community_welfare_guide`** —   
  <sub>args: need</sub>

## Example

```python
from church_mcp.server import denomination_directory

result = denomination_directory()
# denominations, structures, welfare programmes, contacts
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "church-mcp": {
      "command": "python",
      "args": ["-m", "church_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

Directory information compiled from public sources and changes as institutions do. Confirm services and contacts directly before travelling to a facility.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

