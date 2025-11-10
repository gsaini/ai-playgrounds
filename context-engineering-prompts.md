# Context Engineering Prompts

This document outlines the structured approach for AI-assisted development workflows, including documentation standards and agent behavior guidelines.

---

## Documentation Structure

All project documentation follows this standardized structure:

```
/docs
├── Implementation.md
├── project_structure.md
├── UI_UX_doc.md
└── Bug_tracking.md
```

See individual files in `/docs` for detailed templates and guidelines.

---

## Development Agent Workflow

### Primary Directive

Follow established documentation and maintain consistency across all deliverables.

---

### Task Execution Protocol

#### Step 1: Task Assessment

- Read subtask from `/docs/Implementation.md`
- Simple subtask → Implement directly
- Complex subtask → Create detailed todo list first

#### Step 2: Documentation Research

- Check `/docs/Implementation.md` for relevant documentation links
- Review official documentation before implementing

#### Step 3: UI/UX Implementation

- Consult `/docs/UI_UX_doc.md` before implementing any UI elements
- Follow design system specifications exactly

#### Step 4: Project Structure Compliance

- Check `/docs/project_structure.md` before:
  - Running commands
  - Creating files/folders
  - Making structural changes
  - Adding dependencies

#### Step 5: Error Handling

- Check `/docs/Bug_tracking.md` for similar issues before fixing
- Document new errors with root cause and solution

#### Step 6: Implementation

- Write clean, maintainable code
- Follow project coding standards
- Ensure proper error handling

#### Step 7: Task Completion

Mark complete ONLY when:

- ✅ All functionality implemented correctly
- ✅ Code follows project structure guidelines
- ✅ UI/UX matches specifications
- ✅ No errors or warnings remain
- ✅ Documentation updated

---

### File Reference Priority

1. `/docs/Bug_tracking.md` - Check for known issues first
2. `/docs/Implementation.md` - Main task reference
3. `/docs/project_structure.md` - Structure guidance
4. `/docs/UI_UX_doc.md` - Design requirements

---

## Critical Rules

### NEVER

- ❌ Skip documentation consultation
- ❌ Mark tasks complete without proper testing
- ❌ Ignore project structure guidelines
- ❌ Implement UI without checking UI_UX_doc.md
- ❌ Fix errors without checking Bug_tracking.md first

### ALWAYS

- ✅ Document errors and solutions
- ✅ Follow the established workflow process
- ✅ Maintain consistency with existing code
- ✅ Test thoroughly before marking complete
- ✅ Update documentation when making changes

---

## Summary

This framework ensures structured documentation, clear workflows, reduced errors, and higher quality deliverables through adherence to standards.
