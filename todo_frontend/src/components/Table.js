import React from 'react';


const Table = (props) => (
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {props.data.map(todo => (
                <tr key={todo.id}>
                    <td>
                        {todo.title}
                    </td>
                    <td>
                        {todo.description}
                    </td>
                    <td>
                        {!todo.done ? <button onClick={() => props.onClick(todo.id)}>Finish</button> : 'DONE'}
                    </td>
                </tr>
            ))}
        </tbody>
        <tfoot>
            <p>{props.data.length} todos</p>
        </tfoot>
    </table>
);

export default Table;