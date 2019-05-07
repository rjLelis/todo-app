import React from 'react';


const Table = ({data}) => (
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    {data.title}
                </td>
                <td>
                    {data.description}
                </td>
                <td>
                    {!data.done ? <button>Finish</button> : 'DONE'}
                </td>
            </tr>
        </tbody>
    </table>
);

export default Table;