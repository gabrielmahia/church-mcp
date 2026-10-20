"""ChurchMCP — Kenya Community Religious Institution Infrastructure (6 tools). DEMO."""
from __future__ import annotations

from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(name="church-mcp", instructions="Kenya community and religious institution infrastructure. DEMO.")

@mcp.tool(name="catholic_diocese_finder", description="List sample Catholic dioceses in Kenya by county, with the Kenya Conference of Catholic Bishops and Caritas Kenya pointers. Use when someone asks which diocese covers a county. county filters by matching text; an unmatched county returns a note to check kccb.or.ke. Returns the source label, county, the dioceses and welfare contacts. A short sample labelled DEMO, not the full list. Church-run service counts are rough and unverified. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def catholic_diocese_finder(county: str | None = Field(None, description="Optional filter for county. Pass None to return all results.")) -> dict:
    DIOCESES = [
        {"name": "Archdiocese of Nairobi", "counties": ["Nairobi", "Kiambu"], "parishes": "80+", "contact": "archdioceseofnairobi.org"},
        {"name": "Diocese of Mombasa", "counties": ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu"], "contact": "catholicmombasa.org"},
        {"name": "Diocese of Kisumu", "counties": ["Kisumu", "Siaya"], "contact": "kisumucatholic.org"},
        {"name": "Diocese of Nakuru", "counties": ["Nakuru", "Narok", "Kericho"], "contact": "nakurudiocese.org"},
        {"name": "Diocese of Eldoret", "counties": ["Uasin Gishu", "Trans Nzoia", "West Pokot"], "contact": "eldoretdiocese.org"},
        {"name": "Archdiocese of Nyeri", "counties": ["Nyeri", "Laikipia", "Nyandarua"], "contact": "nyeridiocese.org"},
    ]
    if county:
        matched = [d for d in DIOCESES if any(county.lower() in c.lower() for c in d.get("counties", []))]
        return {"source": "DEMO — Kenya Conference of Catholic Bishops", "county": county,
                "dioceses": matched or [{"note": "Check kccb.or.ke for full list"}]}
    return {"source": "DEMO — KCCB", "dioceses": DIOCESES, "kccb": "kccb.or.ke",
            "welfare": "Caritas Kenya: caritaskenya.org",
            "note": "About a fifth of Kenyans are Catholic by commonly cited estimates (sources differ: check the 2019 census religion tables). Church-run health and school counts are rough and unverified."}

@mcp.tool(name="protestant_denomination_guide", description="Overview of major Protestant and Pentecostal denominations in Kenya (ACK, PCEA, AIC, SDA, MCK, Pentecostal churches) with indicative membership, contacts and welfare work. Use when someone asks about a denomination. Takes no arguments. Returns the source label, the denominations and the NCCK pointer. Membership figures are rough, unverified estimates labelled DEMO, and religious shares differ between sources: check the 2019 census tables. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def protestant_denomination_guide() -> dict:
    return {"source": "DEMO — NCCK Kenya", "denominations": {
        "ACK": {"full": "Anglican Church of Kenya", "members_m": 5.0, "contact": "ackenya.com", "welfare": "Hospitals, schools, development"},
        "PCEA": {"full": "Presbyterian Church of East Africa", "members_m": 4.0, "contact": "pcea.or.ke", "notable": "Kikuyu Hospital"},
        "AIC": {"full": "Africa Inland Church", "members_m": 3.0, "contact": "aickenya.com", "welfare": "Tenwek Hospital, Kijabe Hospital"},
        "SDA": {"full": "Seventh-day Adventist", "members_m": 2.0, "contact": "adventistkenya.org"},
        "MCK": {"full": "Methodist Church Kenya", "members_m": 1.5, "contact": "methodistkenya.org"},
        "Pentecostal": {"full": "Various (PEFA, PAG, Deliverance Church etc)", "members_m": 8.0, "note": "Fastest growing"},
    }, "ncck": "National Council of Churches of Kenya: ncck.or.ke",
        "protestant_pct": "Protestant and other Christian denominations together are the majority of Kenyans; shares differ by source, so check the 2019 census religion tables."}

@mcp.tool(name="muslim_community_guide", description="Overview of Kenya's Muslim community: where it is concentrated, major organisations such as SUPKEM, notable mosques and halal certification. Use when someone asks about Muslim organisations or institutions. county is only echoed back as a focus label. Returns the source label, the community overview (about 11% of the population in the 2019 census), organisations, mosques, halal certification and the county focus. A short overview labelled DEMO. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def muslim_community_guide(county: str | None = Field(None, description="County to find Muslim community resources in.")) -> dict:
    """Return Muslim community organisations, mosques, and welfare services in Kenya."""
    return {"source": "DEMO", "kenya_muslims": "~11% of Kenya population. Concentrated in Coast, North Eastern, Nairobi Eastleigh",
            "organizations": [
                {"name": "SUPKEM", "full": "Supreme Council of Kenya Muslims", "contact": "supkem.or.ke", "role": "Umbrella body, halal certification"},
                {"name": "CIPK", "full": "Council of Imams and Preachers of Kenya", "contact": "cipk.or.ke"},
                {"name": "Islamic Foundation of Kenya", "contact": "islamicfoundation.or.ke", "role": "Education, welfare"},
            ],
            "major_mosques": [
                {"name": "Jamia Mosque", "location": "Nairobi CBD", "capacity": 3000},
                {"name": "Mandhry Mosque", "location": "Mombasa Old Town", "est": "1570 (oldest mosque in Kenya)"},
            ],
            "halal": "Halal certification: SUPKEM | Kenya Bureau of Standards (KEBS)",
            "county_focus": county or "All counties"}

@mcp.tool(name="religious_community_services", description="Education, health and welfare services run by religious communities in Kenya, with examples. Use when someone asks what help faith institutions provide. Takes no arguments. Returns the source label, the services by area and a key principle. Counts such as numbers of schools are rough and unverified, labelled DEMO. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def religious_community_services() -> dict:
    return {"source": "DEMO", "services": {
        "education": "Catholic: ~3,000 schools. ACK/AIC/PCEA: ~2,000 schools. Islamic madrasa: ~200 centres.",
        "health": "Kijabe (AIC), Tenwek (AIC), Consolata Nyeri (Catholic), Kikuyu Hospital (PCEA), Aga Khan (Ismaili)",
        "welfare": "Caritas Kenya (Catholic), NCCK programs (Protestant), Zakat distribution (Muslim)",
        "bursaries": "Most parishes, churches, and mosques offer education bursaries. Contact local leadership.",
        "dispute_resolution": "Religious leaders serve as trusted mediators — often faster and cheaper than courts.",
    }, "key_principle": "Religious institutions are Kenya's most accessible welfare network, especially outside Nairobi."}

@mcp.tool(name="church_legal_registration", description="Legal routes for registering a church or religious body in Kenya (society, trust, NGO or company) with the law, fee, timeline and best use. Use when someone wants to set up a congregation or organisation. Takes no arguments. Returns the source label, the options, the registrar contact and a disclaimer. Fees and timelines are indicative and labelled DEMO and not legal advice: consult an advocate. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def church_legal_registration() -> dict:
    return {"source": "DEMO — Societies Act, NGO Coordination Board",
            "options": {
                "society": {"law": "Societies Act Cap 108", "fee_kes": 1000, "timeline": "3-6 months", "best_for": "Small churches"},
                "trust": {"law": "Trustees (Perpetual Succession) Act", "best_for": "Property-owning churches"},
                "ngo": {"law": "NGO Coordination Act", "fee_kes": 10000, "best_for": "Organizations with international funding"},
                "company": {"law": "Companies Act 2015", "platform": "ecitizen.go.ke", "best_for": "Commercial religious arms"},
            },
            "registrar_of_societies": "attorney-general.go.ke | 020-2227461",
            "disclaimer": "Not legal advice. Consult an advocate."}

@mcp.tool(name="community_welfare_guide", description="Where to get food, medical, education and other welfare help through faith-based and community programmes in Kenya. Use when someone asks where to find help. need matches by name or text; if none match, ALL programmes are returned. Returns the source label, the need and the guidance, and how to access help. A short list labelled DEMO: confirm availability with the organisation. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def community_welfare_guide(need: str | None = Field(None, description="Optional filter for need. Pass None to return all results.")) -> dict:
    PROGRAMS = {
        "food_emergency": "Caritas Kenya (Catholic), NCCK (Protestant), mosque sadaqah funds",
        "medical_support": "Mission hospitals cross-subsidise uninsured patients. Tell the accounts desk your situation.",
        "education_bursary": "Apply through local parish/church/mosque. Bishop bursary (ACK). Parish committees (Catholic).",
        "counselling": "Pastoral counselling at most churches and mosques. Ask your priest/pastor/imam.",
        "funeral_support": "Church welfare committees often assist members. Chama within the congregation.",
        "women_safety": "Women groups in churches/mosques. FIDA Kenya: fidakenya.org | Gender Violence Recovery Centre",
        "youth": "Parish youth groups, mosque youth centres, church sports. Contact local leadership.",
    }
    if need:
        n = need.lower()
        matched = {k: v for k, v in PROGRAMS.items() if n in k or n in v.lower()}
        return {"source": "DEMO", "need": need, "guidance": matched or PROGRAMS}
    return {"source": "DEMO", "programs": PROGRAMS,
            "how_to_access": "Visit your nearest church or mosque. Most communities welcome those in need regardless of membership status."}

def main() -> None:
    """Console entry point."""
    mcp.run()
