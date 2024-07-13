import React from 'react';
import {
  Container,
  Divider,
  Dropdown,
  Grid,
  Header,
  Image,
  List,
  Menu,
  Segment,
} from 'semantic-ui-react';

const FixedMenuLayout = () => (
  <div>
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header>
          <Image size='mini' src='/logo.png' style={{ marginRight: '1.5em' }} />
          FastAPI-Template-Project
        </Menu.Item>
        {/* Commenting out the dropdown menu */}
        {/*
        <Dropdown item simple text='Dropdown'>
          <Dropdown.Menu>
            <Dropdown.Item>List Item</Dropdown.Item>
            <Dropdown.Item>List Item</Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Header>Header Item</Dropdown.Header>
            <Dropdown.Item>
              <i className='dropdown icon' />
              <span className='text'>Submenu</span>
              <Dropdown.Menu>
                <Dropdown.Item>List Item</Dropdown.Item>
                <Dropdown.Item>List Item</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown.Item>
            <Dropdown.Item>List Item</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        */}
        {/* Change "Home" to "Github code" */}
        <Menu.Item as='a' href='https://github.com/Bazoopa/FastAPI-PyPoetry-Template' target='_blank'>
          GitHub Code
        </Menu.Item>
      </Container>
    </Menu>

    <Container text style={{ marginTop: '7em' }}>
      <Header as='h1'>FastAPI-Template-Project:</Header>
      <p>The following project is supposed to act as a starting point for more complex projects. It’s primarily focused on good design rather than features so that the project can be forked, and features can be added depending on the requirements of the project.
To show basic functionality of a full stack FastAPI project to show how the template works, below is an example of a simple Thread based chat system that can be used. Please feel free to give it a try (In good faith!).
</p>
      <p>

      </p>

 {/*      <Image src='/images/wireframe/media-paragraph.png' style={{ marginTop: '2em' }} />
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />
      */}
      <Image src='/images/wireframe/paragraph.png' style={{ marginTop: '2em' }} />

      <p>
      </p>
<div>
  <h1>Tech Stack Summary</h1>

  <p>
    This document outlines the technology stack used in the project, encompassing both backend and frontend components. The project leverages modern tools and frameworks to ensure robustness, scalability, and maintainability throughout development and deployment phases.
  </p>

  <h2>Backend Technologies</h2>
  <ul>
    <li>
      <strong>Framework:</strong> FastAPI, a Python web framework for building APIs with high performance and type annotations.
    </li>
    <li>
      <strong>Database:</strong> MySQL hosted on Azure, providing a reliable and scalable storage solution.
    </li>
    <li>
      <strong>Package Management:</strong> Python Poetry for managing dependencies and environment settings.
    </li>
    <li>
      <strong>Deployment:</strong> Docker containers orchestrated with Docker Compose, hosted on Azure for scalable and consistent deployment.
    </li>
  </ul>

  <h2>Frontend Technologies</h2>
  <ul>
    <li>
      <strong>Framework:</strong> React, a JavaScript library for building user interfaces with a focus on reusability and component-based architecture.
    </li>
  </ul>

  <h2>Production</h2>

  <h3>Database</h3>
  <ul>
    <li>
      <strong>MySQL hosted on Azure</strong>
      <ul>
        <li>
          <strong>MySQL:</strong> A popular open-source relational database management system. MySQL is used to store and manage the project's data.
        </li>
        <li>
          <strong>Azure:</strong> Microsoft's cloud computing platform, which hosts the MySQL database to ensure scalability, security, and availability.
        </li>
      </ul>
    </li>
  </ul>

  <h3>CI/CD</h3>
  <ul>
    <li>
      <strong>GitHub</strong>
      <ul>
        <li>
          <strong>GitHub Workflow:</strong> Utilized for continuous integration and continuous deployment (CI/CD). A workflow is configured to automatically run tests whenever code is pushed to the main branch. This ensures code quality and prevents integration issues.
        </li>
      </ul>
    </li>
  </ul>

  <h3>Framework</h3>
  <ul>
    <li>
      <strong>FastAPI:</strong> A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. FastAPI allows for quick development of robust and production-ready APIs.
    </li>
  </ul>

  <h3>Package Manager</h3>
  <ul>
    <li>
      <strong>Python Poetry:</strong> A dependency management and packaging tool for Python. Poetry helps manage project dependencies and packaging, ensuring a smooth and reproducible environment setup.
    </li>
  </ul>

  <h3>Packages</h3>
  <ul>
    <li>
      The project relies on the following Python packages:
      <ul>
        <li><strong>Python:</strong> ^3.9 - The programming language used for the project.</li>
        <li><strong>FastAPI:</strong> ^0.111.0 - The web framework for building the API.</li>
        <li><strong>Uvicorn:</strong> ^0.30.1 - A lightning-fast ASGI server implementation, used to serve FastAPI applications.</li>
        <li><strong>NumPy:</strong> ^2.0.0 - A fundamental package for scientific computing with Python.</li>
        <li><strong>SQLAlchemy:</strong> ^2.0.31 - An SQL toolkit and Object-Relational Mapping (ORM) library for Python.</li>
        <li><strong>aiomysql:</strong> ^0.2.0 - A library for accessing a MySQL database from the asyncio framework.</li>
        <li><strong>mysql-connector-python:</strong> ^9.0.0 - A MySQL database connector for Python.</li>
        <li><strong>python-dotenv:</strong> ^1.0.1 - A tool to read and set environment variables from a .env file.</li>
        <li><strong>Flake8:</strong> ^7.1.0 - A tool for enforcing coding style (PEP 8) in Python projects.</li>
        <li><strong>Pandas:</strong> ^2.2.2 - A library providing high-performance, easy-to-use data structures and data analysis tools for Python.</li>
      </ul>
    </li>
  </ul>

  <h3>Docker</h3>

  <h4>Docker and Docker Compose</h4>
  <ul>
    <li>
      <strong>Docker:</strong> Containerization platform used to package the application and its dependencies into standardized units (containers). Docker ensures consistency across development, testing, and deployment environments.
    </li>
    <li>
      <strong>Docker Compose:</strong> Tool for defining and running multi-container Docker applications. It simplifies the process of orchestrating multiple Docker containers and services.
    </li>
    <li>
      <strong>Azure:</strong> The project is hosted on Microsoft Azure, leveraging its cloud services for deployment and scalability.
    </li>
  </ul>

  <h4>Docker Containers</h4>
  <ul>
    <li>
      <strong>Backend:</strong> FastAPI application is containerized using Docker to ensure it runs consistently across different environments.
    </li>
    <li>
      <strong>Frontend:</strong> React application is containerized using Docker, providing a portable and consistent environment for the frontend.
    </li>
  </ul>

  <h2>Frontend</h2>

  <h3>Framework</h3>
  <ul>
    <li>
      <strong>React:</strong> A JavaScript library for building user interfaces. React is used for developing the frontend of the application, providing a responsive and interactive user experience.
    </li>
  </ul>

  <h2>Testing and CI/CD</h2>
  <ul>
    <li>
      <strong>Testing:</strong> Pytest for backend testing with an in-memory SQLite database for fast, isolated tests.
    </li>
    <li>
      <strong>CI/CD:</strong> GitHub Actions configured to automate testing upon code commits to ensure code quality and integration readiness.
    </li>
  </ul>

  <h2>Additional Tools</h2>
  <ul>
    <li>
      <strong>Environment Management:</strong> .env files for managing environment variables securely.
    </li>
  </ul>
</div>


    </Container>

    <Segment inverted vertical style={{ margin: '5em 0em 0em', padding: '5em 0em' }}>
      <Container textAlign='center'>
        <Grid divided inverted stackable>
          <Grid.Column width={3}>
            <Header inverted as='h4' content='Group 1' />
            <List link inverted>
              <List.Item as='a'>Link One</List.Item>
              <List.Item as='a'>Link Two</List.Item>
              <List.Item as='a'>Link Three</List.Item>
              <List.Item as='a'>Link Four</List.Item>
            </List>
          </Grid.Column>
          <Grid.Column width={3}>
            <Header inverted as='h4' content='Group 2' />
            <List link inverted>
              <List.Item as='a'>Link One</List.Item>
              <List.Item as='a'>Link Two</List.Item>
              <List.Item as='a'>Link Three</List.Item>
              <List.Item as='a'>Link Four</List.Item>
            </List>
          </Grid.Column>
          <Grid.Column width={3}>
            <Header inverted as='h4' content='Group 3' />
            <List link inverted>
              <List.Item as='a'>Link One</List.Item>
              <List.Item as='a'>Link Two</List.Item>
              <List.Item as='a'>Link Three</List.Item>
              <List.Item as='a'>Link Four</List.Item>
            </List>
          </Grid.Column>
          <Grid.Column width={7}>
            <Header inverted as='h4' content='Footer Header' />
            <p>
              Extra space for a call to action inside the footer that could help re-engage users.
            </p>
          </Grid.Column>
        </Grid>

        <Divider inverted section />
        <Image centered size='mini' src='/logo.png' />
        <List horizontal inverted divided link size='small'>
          <List.Item as='a' href='#'>
            Site Map
          </List.Item>
          <List.Item as='a' href='#'>
            Contact Us
          </List.Item>
          <List.Item as='a' href='#'>
            Terms and Conditions
          </List.Item>
          <List.Item as='a' href='#'>
            Privacy Policy
          </List.Item>
        </List>
      </Container>
    </Segment>
  </div>
);

export default FixedMenuLayout;
