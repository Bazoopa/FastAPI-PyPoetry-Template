import React from 'react';
import {
  Container,
  Menu,
  Segment,
  Header,
  Image,
  Grid,
  List,
  Divider
} from 'semantic-ui-react';
import ChatList from './components/ChatList';
import MessageList from './components/MessageList';



const App = () => {
  return (
    <div>
      <Menu fixed='top' inverted>
        <Container>
          <Menu.Item as='a' header>
            <Image size='mini' src='/logo.png' style={{ marginRight: '1.5em' }} />
            FastAPI-Template-Project
          </Menu.Item>
          <Menu.Item as='a' href='https://github.com/Bazoopa/FastAPI-PyPoetry-Template' target='_blank'>
            GitHub Code
          </Menu.Item>
        </Container>
      </Menu>




      <Container text style={{ marginTop: '7em' }}>
        <Header as='h3'>FastAPI-Template-Project:</Header>
        <p>
          The following project is supposed to act as a starting point for more complex projects.
          It’s primarily focused on good design rather than features so that the project can be forked,
          and features can be added depending on the requirements of the project.
          To show basic functionality of a full stack FastAPI project to show how the template works,
          below is an example of a simple Thread based chat system that can be used as a starting point for other projects.
          Please feel free to give it a try (In good faith!).
        </p>





  return (
    <div>
      <h2>All Chats</h2>
      <ul>
        {chats.map(chat => (
          <li key={chat.id} onClick={() => handleChatSelect(chat.id)}>
            {chat.name}
          </li>
        ))}
      </ul>
      {selectedChatId !== null && <MessageList chatId={selectedChatId} />}
    </div>
  );
};






        <div>
          <h4>Stack:</h4>
          <h4>Backend Technologies:</h4>
          <ul>
            <li><strong>Framework:</strong> FastAPI</li>
            <li><strong>Database:</strong> MySQL on Azure</li>
            <li><strong>Package Management:</strong> Python Poetry</li>
            <li><strong>Deployment:</strong> Docker Compose on Azure</li>
          </ul>
          <h4>Frontend Technologies</h4>
          <ul>
            <li><strong>Framework:</strong> React</li>
          </ul>
          <h4>Testing and CI/CD</h4>
          <ul>
            <li><strong>Testing:</strong> Pytest with SQLite</li>
            <li><strong>CI/CD:</strong> GitHub Actions</li>
          </ul>
          <h4>Additional Tools</h4>
          <ul>
            <li><strong>Environment Management:</strong> .env files</li>
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
};

export default App;
