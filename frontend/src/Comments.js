import React, { useEffect, useState } from 'react'
import {Navbar, Card, Button} from 'react-bootstrap'

function Comments(props) {
    const comments = props.comments
    
    return (<>
        {comments.map((u, key) => (
            <Card key={key}>
                <Card.Body>
                    <pre style={{fontSize:"1.2em"}}>{u.content}</pre>
                </Card.Body>
            </Card>
        ))}
        
    </>)
}
export default Comments
