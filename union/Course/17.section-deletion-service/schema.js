const { gql } = require('apollo-server');

module.exports = gql`
  type Mutation {
    deleteSection(id: ID!): String
  }

  type Query {
    _empty: String
  }
`;