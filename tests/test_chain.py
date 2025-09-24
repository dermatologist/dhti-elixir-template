import pytest
import requests


@pytest.fixture
def chain():
    from src.dhti_elixir_template import DhtiChain
    return DhtiChain().get_chain_as_langchain_tool()


def test_chain_invoke(chain, capsys):
    input_data = {"input": "Answer in one word: What is the capital of France?"}
    result = chain.invoke(input=input_data)  # type: ignore
    print(result)
    captured = capsys.readouterr()
    assert "Paris" in captured.out or "know" in captured.out


def test_chain_invoke_with_hook(chain, capsys):
    input_data = {"input":{
        "hookInstance": "test_hook",
        "fhirServer": "http://example.com/fhir",
        "fhirAuthorization": "Bearer test_token",
        "hook": "patient-view",
        "context": {"input": "Hello"},
        "prefetch": {},
    }}
    result = chain.invoke(input=input_data)  # type: ignore
    print(result)
    captured = capsys.readouterr()
    assert "Paris" in captured.out or "know" in captured.out

def test_chain_invoke_with_request(chain, capsys):
    input_data = {"input":{
        "hookInstance": "9a9f10a0-0f99-4471-8d98-b44b854ca079",
        "hook": "order-select",
        "fhirServer": "http://hapi.fhir.org/baseR4",
        "context": {
            "patientId": "48596990",
            "userId": "Practitioner/COREPRACTITIONER1",
            "selections": ["MedicationRequest/request-123"],
            "draftOrders": {
                "resourceType": "Bundle",
                "entry": [
                    {
                        "resource": {
                            "resourceType": "MedicationRequest",
                            "id": "request-123",
                            "status": "draft",
                            "subject": {"reference": "Patient/48596990"},
                            "authoredOn": "2025-09-21",
                        }
                    },
                    {
                        "resource": {
                            "resourceType": "CommunicationRequest",
                            "id": "commreq-20250921104547",
                            "status": "active",
                            "subject": {"reference": "Patient/48596990"},
                            "payload": [
                                {
                                    "contentString": "Hello is this doing this doing man? Hello? predict this face this too,by the way gh"
                                }
                            ],
                            "priority": "routine",
                            "authoredOn": "2025-09-21T15:45:47.640Z",
                        }
                    },
                ],
            },
        },
        "prefetch": {
            "patient": {
                "resourceType": "Patient",
                "id": "48596990",
                "meta": {
                    "versionId": "1",
                    "lastUpdated": "2025-08-06T12:52:20.638+00:00",
                    "source": "#dUTRcmjB7oZi7Gh5",
                },
                "text": {
                    "status": "generated",
                    "div": '<div xmlns="http://www.w3.org/1999/xhtml"><div class="hapiHeaderText">NuÃ±ez <b>KARLA </b></div><table class="hapiPropertyTable"><tbody><tr><td>Date of birth</td><td><span>02 January 1980</span></td></tr></tbody></table></div>',
                },
                "name": [{"family": "Karla", "given": ["NuÃ±ez"]}],
                "gender": "female",
                "birthDate": "1980-01-02",
            }
        },
    }}
    result = chain.invoke(input=input_data)  # type: ignore
    print(result)
    captured = capsys.readouterr()
