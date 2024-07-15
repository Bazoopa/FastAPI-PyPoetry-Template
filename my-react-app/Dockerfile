# Dockerfile for React app
FROM node:14-alpine

WORKDIR /app

# Copy package.json and package-lock.json to the WORKDIR
COPY package*.json ./

# Install npm dependencies
RUN npm install

# Install axios specifically
RUN npm install axios

# Copy the rest of the application code
COPY . .

# Expose the port your React app runs on
EXPOSE 3000

# Start the React application
CMD ["npm", "start"]
