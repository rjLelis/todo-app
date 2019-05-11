import React from 'react';


const Table = props => (
    <table className='table'>
        <thead className="thead-dark">
            <tr>
                <th scope='col'>Title</th>
                <th scope='col'>Description</th>
                <th scope='col'></th>
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
                    <td className={!todo.done ? '' : 'alert-success'}>
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