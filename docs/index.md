# dhti-elixir-template

[![Release](https://img.shields.io/github/v/release/dermatologist/dhti-elixir-template)](https://img.shields.io/github/v/release/dermatologist/dhti-elixir-template)
[![Build status](https://img.shields.io/github/actions/workflow/status/dermatologist/dhti-elixir-template/main.yml?branch=main)](https://github.com/dermatologist/dhti-elixir-template/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/dermatologist/dhti-elixir-template)](https://img.shields.io/github/commit-activity/m/dermatologist/dhti-elixir-template)
[![License](https://img.shields.io/github/license/dermatologist/dhti-elixir-template)](https://img.shields.io/github/license/dermatologist/dhti-elixir-template)

This is a template repository for creating DHTI elixir projects. DHTI elixirs provide backend GenAI capabilities as HTTP endpoints hosted by LangServe, with integrated FHIR support for clinical decision support systems.

## Features

- Template for building LangServe-based backend services
- Integration with FHIR for healthcare data
- Support for CDS Hooks protocol
- Multiple implementation patterns (chain, agent, advanced agent)
- AI agent skills for automatic project generation

## AI Agent Skills

This repository includes AI agent skills that can automatically generate new DHTI elixir projects. The skills guide agents through:

- Environment setup and project scaffolding
- Implementation of FHIR-based data retrieval
- LangChain chain development
- Testing and documentation

Skills are located in `.github/skills/elixir-generator/` (preferred) and `.claude/skills/elixir-generator/` (legacy).
