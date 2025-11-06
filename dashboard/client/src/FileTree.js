import React from 'react';
import { Accordion, AccordionSummary, AccordionDetails, Card, CardActionArea, Typography, Box } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import FolderIcon from '@mui/icons-material/Folder';
import ArticleIcon from '@mui/icons-material/Article';

function FileTree({ fileStructure, onFileSelect }) {
  const renderTree = (nodes) => {
    return nodes.map((node) => {
      if (node.type === 'directory') {
        return (
          <Accordion key={node.path} sx={{ boxShadow: 'none', '&:before': { display: 'none' } }}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Box sx={{ display: 'flex', alignItems: 'center' }}>
                <FolderIcon sx={{ mr: 1, color: 'primary.main' }} />
                <Typography>{node.name}</Typography>
              </Box>
            </AccordionSummary>
            <AccordionDetails sx={{ pl: 4 }}>
              {node.children && renderTree(node.children)}
            </AccordionDetails>
          </Accordion>
        );
      } else {
        return (
          <Card key={node.path} sx={{ mb: 1, backgroundColor: '#f9f9f9' }}>
            <CardActionArea onClick={() => onFileSelect(node.path)}>
              <Box sx={{ display: 'flex', alignItems: 'center', p: 1 }}>
                <ArticleIcon sx={{ mr: 1, color: 'grey.700' }} />
                <Typography variant="body2">{node.name}</Typography>
              </Box>
            </CardActionArea>
          </Card>
        );
      }
    });
  };

  return <div>{renderTree(fileStructure)}</div>;
}

export default FileTree;
