# MSDBOK - Managing Software Development Body of Knowledge

A comprehensive course handbook and knowledge repository for **Managing Software Development**, covering key topics in software project management, team leadership, and development processes.

**Live Site:** [msdbok.github.io](https://msdbok.github.io)

## About

This repository contains structured course notes and resources designed for MS students, professionals, and anyone interested in learning about software development management. The content focuses on breadth over depth, introducing a wide range of concepts and practices while emphasizing critical thinking and decision-making.

## Content Areas

The handbook is organized into 7 major knowledge areas:

1. **[People](content/people/)** - Managing technical teams, motivation, and decision-making
2. **[Processes](content/proc/)** - Project lifecycle stages, frameworks, and process selection
3. **[Needs](content/needs/)** - Customer expectations, requirements, and risk management
4. **[Scope](content/scope/)** - Work Breakdown Structure (WBS) and estimation methods
5. **[Planning](content/plan/)** - Agile vs plan-driven approaches, Gantt charts, critical path
6. **[Tracking](content/track/)** - Progress monitoring, burndown charts, Earned Value Management
7. **[Materials](content/material/)** - Curated resources, books, and research papers

## Technology Stack

- **Jekyll** (v4.4.1) - Static site generator
- **Just the Docs** - Documentation theme
- **jekyll-scholar** - Bibliography and citation management (IEEE style)
- **GitHub Pages** - Hosting and deployment

## Building Locally

### Prerequisites

- Ruby 3.3 or higher
- Bundler

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/msdbok/msdbok.github.io.git
   cd msdbok.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Build and serve locally:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser to `http://localhost:4000`

## Project Structure

```
.
├── content/           # Main course content organized by topic
│   ├── people/       # Team management and leadership
│   ├── proc/         # Processes and frameworks
│   ├── needs/        # Requirements and risk management
│   ├── scope/        # Work breakdown and estimation
│   ├── plan/         # Planning approaches
│   ├── track/        # Progress tracking methods
│   └── material/     # Curated resources
├── _includes/        # Reusable Jekyll components
├── _layouts/         # Page layout templates
├── _sass/            # Stylesheets and color schemes
├── _bibliography/    # Bibliography files for citations
└── images/           # Static assets
```

## Contributing

Contributions are welcome! We accept:
- **Content fixes**: typos, fact checks, source validation, clarifications
- **Method descriptions**: 1-2 page focused technique descriptions
- **Comparative analyses**: 3-4 page papers comparing different approaches

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines and templates.

**Quick start:**
- Use [templates/method-template.md](templates/method-template.md) for new methods
- Use [templates/analysis-template.md](templates/analysis-template.md) for comparative papers
- Follow the atomic page principle - each page is self-contained
- Include proper citations and sources

## Deployment

The site is automatically built and deployed to GitHub Pages via GitHub Actions whenever changes are pushed to the `main` branch.

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE).

You are free to share and adapt the material for any purpose, even commercially, as long as you give appropriate credit.

## Author

**Andrey Sadovykh**

## Acknowledgments

Much of the content in this handbook is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management at Carnegie Mellon University. The structure, examples, and pedagogical approach throughout the planning, processes, and materials sections reflect their teaching materials and frameworks.

Pages with significant lecture-based content include an **Acknowledgments section** crediting the original instructors, along with proper citations in the **Sources section**.

## Attribution and Citations

This project maintains rigorous attribution practices:

- **All content pages** include a Sources section with full citations
- **Lecture-based materials** have dedicated Acknowledgments sections
- **Academic citations** follow IEEE style via jekyll-scholar
- **Original frameworks and methods** are attributed to their creators

See our [Citation Standardization Plan](docs/citation-standardization-plan.md) for details on our citation practices.

## Disclaimer

AI tools were used for text polishing and improving explanations. All facts and claims have been verified by the authors.

In case of an error, feel free to [file an issue](https://github.com/msdbok/msdbok.github.io/issues).
