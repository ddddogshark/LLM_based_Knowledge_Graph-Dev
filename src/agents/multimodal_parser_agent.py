from .base_agent import BaseAgent
from typing import Dict, Any, List
import os

class MultimodalParserAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses multimodal materials from the specified data path. It processes a single
        course directory, creating one aggregated markdown file for the entire course,
        named after the course.
        """
        data_path = initial_context.get("data_path")
        course_name = initial_context.get("course_name", "parsed_course")

        self._log(f"Starting multimodal parsing for course '{course_name}' from base path: {data_path}")

        if not data_path or not os.path.exists(data_path):
            self._log(f"Data path not found: {data_path}")
            initial_context["multimodal_parsed_content"] = []
            initial_context["image_paths"] = []
            return initial_context

        all_parsed_content = []
        all_image_paths = []
        parsed_lectures_for_course = []
        image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp"}

        def find_files_recursively(directory: str, extensions: set) -> List[str]:
            found_files = []
            if not os.path.exists(directory):
                return found_files
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    found_files.extend(find_files_recursively(item_path, extensions))
                elif os.path.splitext(item)[1].lower() in extensions:
                    found_files.append(item_path)
            return found_files

        # Find all markdown files in the entire course directory
        md_files = find_files_recursively(data_path, {".md"})
        
        for md_file_path in md_files:
            try:
                with open(md_file_path, "r", encoding="utf-8") as f:
                    md_content = f.read()
            except Exception as e:
                self._log(f"Error reading markdown file {md_file_path}: {e}")
                continue

            # Find associated images, assuming they are in a sibling 'images' directory
            md_dir = os.path.dirname(md_file_path)
            images_dir = os.path.join(md_dir, 'images')
            image_paths = find_files_recursively(images_dir, image_extensions)
            
            # Use relative path for lecture name
            lecture_name = os.path.relpath(md_dir, data_path)

            parsed_lectures_for_course.append({
                "lecture": lecture_name,
                "content": md_content,
                "images": image_paths,
            })
            all_parsed_content.append(md_content)
            all_image_paths.extend([{"course": course_name, "lecture": lecture_name, "path": img} for img in image_paths])

        # Write the aggregated content for the entire course to a single .md file
        if parsed_lectures_for_course:
            # Sanitize course_name for use in filename
            sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip()
            sanitized_course_name = sanitized_course_name.replace(' ', '_')
            output_filename = f"{sanitized_course_name}.md"

            try:
                with open(output_filename, "w", encoding="utf-8") as f:
                    f.write(f"# Course: {course_name}\n\n")
                    for lecture in parsed_lectures_for_course:
                        f.write(f"## Lecture: {lecture['lecture']}\n\n")
                        f.write(lecture['content'])
                        f.write("\n\n")
                        if lecture['images']:
                            f.write("### Images:\n")
                            for img_path in lecture['images']:
                                relative_img_path = os.path.relpath(img_path, os.getcwd())
                                f.write(f"- {relative_img_path}\n")
                            f.write("\n")
                        f.write("---\n\n")
                self._log(f"Successfully generated markdown file for course '{course_name}' at '{output_filename}'.")
            except Exception as e:
                self._log(f"Error writing markdown file for course {course_name}: {e}")

        initial_context["multimodal_parsed_content"] = all_parsed_content
        initial_context["image_paths"] = all_image_paths
        self._log(f"Finished parsing. Found content for {len(all_parsed_content)} markdown files and {len(all_image_paths)} images in total.")
        return initial_context