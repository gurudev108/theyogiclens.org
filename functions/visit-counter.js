/*
const faunadb = require('faunadb');

const q = faunadb.query;
const client = new faunadb.Client({ secret: process.env.FAUNADB_SECRET });

exports.handler = async (event, context) => {
  try {
    const result = await client.query(
      q.If(
        q.Exists(q.Collection('visits')),
        q.Let(
          {
            doc: q.Get(q.Collection('visits')),
            newCount: q.Add(q.Select(['data', 'count'], q.Var('doc')), 1)
          },
          q.Update(q.Select(['ref'], q.Var('doc')), { data: { count: q.Var('newCount') } })
        ),
        q.Create(q.Collection('visits'), { data: { count: 1 } })
      )
    );

    return {
      statusCode: 200,
      body: JSON.stringify({ count: result.data.count })
    };
  } catch (error) {
    return { statusCode: 500, body: error.toString() };
  }
};
*/
