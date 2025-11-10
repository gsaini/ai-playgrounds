# Project Structure

## Root Directory

```
project-name/
├── src/
├── docs/
├── tests/
├── config/
├── deployment/
├── .gitignore
├── README.md
└── package.json
```

---

## Detailed Structure

### /src - Source Code

```
src/
├── components/
├── pages/
├── services/
├── utils/
├── assets/
├── styles/
└── index.js
```

**Purpose**: Contains all application source code

**Naming Conventions**:

- Components: PascalCase (e.g., `Button.jsx`)
- Services: camelCase with `.service.js` suffix
- Utils: camelCase (e.g., `formatDate.js`)

---

### /src/components - UI Components

```
components/
├── Button/
│   ├── Button.jsx
│   ├── Button.test.js
│   └── Button.module.css
└── Card/
    ├── Card.jsx
    ├── Card.test.js
    └── Card.module.css
```

**Purpose**: Reusable UI components  
**Pattern**: Each component in its own folder with tests and styles

---

### /src/pages - Page Components

```
pages/
├── Home/
├── About/
└── Dashboard/
```

**Purpose**: Page-level components and routing

---

### /src/services - Business Logic

```
services/
├── api.service.js
├── auth.service.js
└── data.service.js
```

**Purpose**: API calls, authentication, data management

---

### /src/utils - Helper Functions

```
utils/
├── formatters.js
├── validators.js
└── constants.js
```

**Purpose**: Utility functions and constants

---

### /src/assets - Static Resources

```
assets/
├── images/
├── fonts/
└── icons/
```

**Purpose**: Static files like images, fonts, icons

---

### /docs - Documentation

```
docs/
├── Implementation.md
├── project_structure.md
├── UI_UX_doc.md
└── Bug_tracking.md
```

**Purpose**: Project documentation

---

### /tests - Test Suites

```
tests/
├── unit/
├── integration/
└── e2e/
```

**Purpose**: All test files organized by type

---

### /config - Configuration Files

```
config/
├── development.json
├── staging.json
└── production.json
```

**Purpose**: Environment-specific configurations

---

### /deployment - Deployment Scripts

```
deployment/
├── docker/
├── scripts/
└── ci-cd/
```

**Purpose**: Deployment configurations and scripts

---

## File Naming Conventions

- **Components**: PascalCase (e.g., `UserProfile.jsx`)
- **Services**: camelCase with suffix (e.g., `auth.service.js`)
- **Utils**: camelCase (e.g., `dateFormatter.js`)
- **Tests**: Same as source with `.test.js` suffix
- **Styles**: Same as component with `.module.css` suffix

---

## Module Organization

- Group by feature when possible
- Keep related files together
- Maintain shallow directory structure
- Use index files for clean imports
