CREATE_ORGANIZATION_REQUEST_MOCK = {
    "name": "Acme Corp",
    "domain": "acme.example.com",
    "timezone": "UTC",
}

CREATE_ORGANIZATION_RESPONSE_201_MOCK = {
    "id": "00000000-0000-0000-0000-000000000001",
    "name": "Acme Corp",
    "domain": "acme.example.com",
    "timezone": "UTC",
    "is_active": True,
}

CREATE_ORGANIZATION_RESPONSE_409_MOCK = {
    "error": "Organization with this domain already exists."
}
