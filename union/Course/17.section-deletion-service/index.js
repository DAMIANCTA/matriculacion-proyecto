require('dotenv').config();
const { ApolloServer } = require('apollo-server');
const typeDefs = require('./schema');
const resolvers = require('./resolvers');

const server = new ApolloServer({ typeDefs, resolvers });

server.listen({ port: process.env.PORT || 3014 }).then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});