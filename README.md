security_incident_response_system/
├── __init__.py
├── main.py
├── alerts/
│   ├── __init__.py
│   ├── models.py         # Definição da classe Alert e outros modelos relacionados
│   └── manager.py        # Implementação do AlertManager com operações CRUD
├── cases/
│   ├── __init__.py
│   ├── models.py         # Definição da classe Case e relacionamentos com alertas
│   └── manager.py        # Implementação do CaseManager com operações CRUD
├── tenants/
│   ├── __init__.py
│   ├── models.py         # Definição da classe Tenant
│   └── manager.py        # Implementação do TenantManager com operações CRUD
├── users/
│   ├── __init__.py
│   ├── models.py         # Definição da classe User
│   └── manager.py        # Implementação do UserManager com operações CRUD
├── notifications/
│   ├── __init__.py
│   ├── notifiers.py      # Implementação dos Notifiers (Email, Slack, Mattermost, etc.)
│   └── manager.py        # Gerencia os canais de notificação e envio de mensagens
├── metrics/
│   ├── __init__.py
│   └── manager.py        # Gerencia métricas e geração de dashboards


├── apis/
│   ├── __init__.py
│   └── api.py            # API para integração e acesso aos principais módulos
├── integrations/
│   ├── __init__.py
│   ├── misp.py           # Integração com o MISP (importação de IOCs)
│   └── mitre.py          # Integração com o MITRE ATT&CK (importação de TTPs)



├── reporting/
│   ├── __init__.py
│   └── case_reporter.py  # Geração de relatórios (Markdown, PDF)

├── knowledgebase/
│   ├── __init__.py
│   └── manager.py        # Gerencia a base de conhecimento (artigos, documentos)
├── timeline/
│   ├── __init__.py
│   └── manager.py        # Gerencia a linha do tempo de eventos (CRUD de eventos)
├── correlation/
│   ├── __init__.py
│   └── engine.py         # Módulo para correlacionar alertas com casos
└── directory/
    ├── __init__.py
    └── ldap_service.py   # Serviço de sincronização de usuários via LDAP (exemplo DIP)
