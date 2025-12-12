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

Contributions are welcome! Whether it's fixing typos, improving explanations, or adding new content, your help is appreciated.

- Follow the existing content structure and style
- Ensure all facts and claims are verified
- Use IEEE citation style for references
- Test changes locally before submitting

## Deployment

The site is automatically built and deployed to GitHub Pages via GitHub Actions whenever changes are pushed to the `main` branch.

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE).

You are free to share and adapt the material for any purpose, even commercially, as long as you give appropriate credit.

## Author

**Andrey Sadovykh**

## Acknowledgments

AI tools were used for text polishing and improving explanations. All facts and claims have been verified by the authors.

## Disclaimer

In case of an error, feel free to [file an issue](https://github.com/msdbok/msdbok.github.io/issues).
